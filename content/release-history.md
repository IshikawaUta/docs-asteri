# Release History

Track the evolution of the Asteri web server.

---

## v1.2.1 (Current)
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
