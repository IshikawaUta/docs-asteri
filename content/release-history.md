# Release History

Track the evolution of the Asteri web server.

---

## v2.2.2 (Current)
*May 19, 2026*

This is a landmark release that transforms Asteri from a high-performance web server into a fully **enterprise-grade production framework**. It delivers native HTTP/3, a C-Extension performance core, integrated telemetry, and a fully enforced static quality pipeline.

### 🚀 New Features

- **Native HTTP/3 (QUIC)**: Full HTTP/3 protocol support with QPACK header compression/decompression, QUIC packet framing, and integrated handshake handling.
- **⚡ C-Extension Parsing Core**: Rewrote the HTTP/1.1 and uWSGI parsers as a native C-Extension (`asteri.fastparser`) for blazing-fast zero-copy buffer throughput. Includes seamless Pure-Python fallback.
- **Prometheus & OpenTelemetry Metrics**: Native Prometheus `0.0.4`-compliant `/metrics` endpoint. Metrics are synchronized across all worker processes via the Stash IPC server.
- **Automated PyPI Publishing**: Secure, passwordless OIDC Trusted Publishing workflow via GitHub Actions — releases to PyPI automatically on every `v*.*.*` git tag push.

### 🛡️ Quality & CI/CD

- **Mypy Static Typing Enforced**: All 41 source files are 100% type-annotated and verified. Zero runtime type-errors guaranteed.
- **Ruff Static Analysis**: Cleaned up 100+ `E701` and `E722` violations. Entire codebase is now strictly PEP-8 compliant.
- **Black Formatting**: Global PEP-8 auto-formatting applied across all 47 Python files.
- **CI Pipeline Hardened**: GitHub Actions now enforces `ruff check` and `mypy` on every push before tests run.

### ✅ Testing

- **87/87 Unit Tests** passing.
- **40/40 CLI Regression Scenarios** verified via `test_asteri_cli.sh`.

---

## v1.2.2
*May 17, 2026*

This release added massive event loop integrations (Tornado), unified visual dashboards, robust ASGI fixes, and comprehensive regression test suites.

### 🚀 New Features

- **Native Tornado Integration**: Added `tornado` and `gtornado` worker classes for high-performance non-blocking async loops.
- **Unified Premium Status Dashboard**: Created a gorgeous, centralized status page builder in glassmorphism UI for all worker classes.
- **Robust Intercept Middleware**: Automated dashboard/log routing inside Tornado workers using transparent WSGI wrapper middlewares.
- **Exhaustive Regression Suite**: Upgraded the CLI test framework to cover 100% of the 36+ CLI options and system arguments.

### 🐛 Bug Fixes

- **FastAPI/Flask ASGI Compatibility**: Fixed the ASGI `__call__` calling convention parameter count bug in modern frameworks.
- **Zero Orphaned Workers**: Fixed potential zombie process hazards during abrupt shutdowns.
- **CI/CD Integration**: Expanded GitHub Actions workflow to include full discover-based unit tests.

---

## v1.2.1
*May 16, 2026*

This is a major stability and architectural update, addressing critical bugs discovered during production stress testing.

### 🚀 New Features

- **Output Capture Support**: Added `--capture-output` to redirect `stdout` and `stderr` to error log files.
- **Dynamic Environment**: Automated resolution of `SERVER_NAME` and `SERVER_PORT` via listener socket metadata.
- **Enhanced GThread**: Better thread pool management with explicit `--threads` support.
- **Streaming Body**: Implemented `WSGIInput` for efficient, memory-safe body streaming of large requests.

### 🐛 Bug Fixes

- **Arbiter**: Fixed a critical bug where the master process exited before reaping worker processes.
- **HTTP/2**: Resolved connection preface data loss during the H2 handshake.
- **uWSGI**: Fixed parsing failures for packets exceeding 4KB.
- **Signal Handling**: Improved `SIGQUIT` and `SIGTERM` behavior for graceful shutdowns.
- **Security**: Added safety limits for large headers (up to 32KB).

---

## v1.1.1
*May 14, 2026*

Improved stability release for the initial version series.

---

## v1.0.1
*May 14, 2026*

Patch release addressing minor CLI inconsistencies and formatting.

---

## v1.0.0
*May 14, 2026*

Initial public release of the Asteri web server.

### ✨ Highlights

- **Multi-Worker Support**: Integrated Sync, GThread, ASGI, and Gevent workers.
- **Protocol Switching**: Automatic detection of HTTP/1.1, HTTP/2, and uWSGI on the same port.
- **Status Dashboard**: Built-in real-time process monitoring at `/asteri-status`.
- **Advanced CLI**: Comprehensive argument system for production tuning.
