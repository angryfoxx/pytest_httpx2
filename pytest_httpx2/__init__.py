from collections.abc import Generator
from operator import methodcaller

import httpx2
import pytest
from pytest import Config, FixtureRequest, MonkeyPatch

from pytest_httpx2._httpx_internals import IteratorStream
from pytest_httpx2._httpx_mock import HTTPXMock
from pytest_httpx2._options import _HTTPXMockOptions
from pytest_httpx2.version import __version__

__all__ = (
    "HTTPXMock",
    "IteratorStream",
    "__version__",
)


def _httpx_mock_options(request: FixtureRequest) -> _HTTPXMockOptions:
    httpx_mock_markers: dict = {}
    for marker_name in ("httpx_mock", "httpx2_mock"):
        for marker in request.node.iter_markers(marker_name):
            httpx_mock_markers = marker.kwargs | httpx_mock_markers
    __tracebackhide__ = methodcaller("errisinstance", TypeError)
    return _HTTPXMockOptions(**httpx_mock_markers)


@pytest.fixture
def httpx_mock(
    monkeypatch: MonkeyPatch,
    request: FixtureRequest,
) -> Generator[HTTPXMock, None, None]:
    options = _httpx_mock_options(request)
    mock = HTTPXMock(options)

    # Mock synchronous requests
    real_handle_request = httpx2.HTTPTransport.handle_request

    def mocked_handle_request(
        transport: httpx2.HTTPTransport, request: httpx2.Request
    ) -> httpx2.Response:
        if options.should_mock(request):
            return mock._handle_request(transport, request)
        return real_handle_request(transport, request)

    monkeypatch.setattr(
        httpx2.HTTPTransport,
        "handle_request",
        mocked_handle_request,
    )

    # Mock asynchronous requests
    real_handle_async_request = httpx2.AsyncHTTPTransport.handle_async_request

    async def mocked_handle_async_request(
        transport: httpx2.AsyncHTTPTransport, request: httpx2.Request
    ) -> httpx2.Response:
        if options.should_mock(request):
            return await mock._handle_async_request(transport, request)
        return await real_handle_async_request(transport, request)

    monkeypatch.setattr(
        httpx2.AsyncHTTPTransport,
        "handle_async_request",
        mocked_handle_async_request,
    )

    yield mock
    try:
        mock._assert_options()
    finally:
        mock.reset()


@pytest.fixture
def httpx2_mock(httpx_mock: HTTPXMock) -> HTTPXMock:
    """Alias of :func:`httpx_mock` for HTTPX2-oriented test suites."""
    return httpx_mock


def pytest_configure(config: Config) -> None:
    marker_signature = (
        "*, assert_all_responses_were_requested=True, "
        "assert_all_requests_were_expected=True, "
        "can_send_already_matched_responses=False, "
        "should_mock=lambda request: True"
    )
    config.addinivalue_line(
        "markers",
        f"httpx_mock({marker_signature}): Configure httpx_mock / httpx2_mock fixtures.",
    )
    config.addinivalue_line(
        "markers",
        f"httpx2_mock({marker_signature}): Configure httpx_mock / httpx2_mock fixtures.",
    )
