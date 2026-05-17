# 👷 Mastering Asteri Worker Models

Choosing the right worker model is the most important decision for maximizing Asteri's performance for your specific application workload. Asteri provides four distinct models to handle everything from simple scripts to massive asynchronous APIs.

## 🏗️ Comparative Overview of Worker Models

### 1. Synchronous Workers (`sync`)

The default worker type. It handles one request at a time per worker process.

- **Best for**: CPU-bound tasks, simple applications, or legacy code that isn't thread-safe.
- **Mechanism**: Standard process-based concurrency. If a request is blocked (e.g., waiting for a database), the entire worker is blocked.

### 2. Threaded Workers (`gthread`)

A multi-threaded worker model where each worker process can handle multiple requests using a thread pool.

- **Best for**: I/O-bound tasks in applications that are thread-safe (e.g., standard Django/Flask apps).
- **Configuration**: Use `--threads` to set the number of threads per worker.
- **Mechanism**: Uses a thread pool to handle concurrent requests within a single process, reducing memory overhead compared to spawning many processes.

### 3. Gevent Workers (`gevent`)

An asynchronous worker based on Greenlets (pseudo-threads) and the Gevent library.

- **Best for**: Extremely high concurrency, long-lived connections, and heavy I/O-bound workloads.
- **Requirement**: Must have `gevent` installed (`pip install gevent`).
- **Mechanism**: Cooperative multitasking. It patches standard library functions to be non-blocking, allowing thousands of concurrent connections in a single process.

### 4. ASGI Workers (`asgi`)

Native support for modern asynchronous applications and protocols (HTTP/2, WebSockets).

- **Best for**: FastAPI, Starlette, and other async frameworks.
- **Mechanism**: Implements the ASGI 3.0 specification. It leverages Python's `asyncio` to handle concurrent requests efficiently.

### 5. Tornado & GTornado Workers (`tornado` / `gtornado`) [NEW]

An asynchronous worker model leveraging Tornado's high-performance non-blocking HTTP server and event loop container.

- **Best for**: WSGI-based applications requiring premium asynchronous connection handling, WebSocket gateways, or event-driven backends.
- **`tornado`**: Standard asynchronous event loop powered by Tornado's native `IOLoop` and `tornado.wsgi.WSGIContainer`.
- **`gtornado`**: Greenlet-enabled cooperative multitasking worker class running Tornado loops for extreme event-driven performance.
- **Native Middleware Interception**: Automatically wraps target applications with `TornadoDashboardMiddleware` under the hood. The `/asteri-status` and system logs are intercepted transparently at the core network level without requiring any custom routes in your code.

## 📊 Comparison Table

| Worker | Concurrency Type | I/O Performance | Complexity | Use Case |
|--------|------------------|-----------------|------------|----------|
| `sync` | Process | Low | Low | Simple/CPU tasks |
| `gthread` | Thread | Medium | Medium | Standard Web Apps |
| `gevent` | Greenlet | High | Medium | High Traffic/Chat |
| `asgi` | AsyncIO | High | High | Modern Async Apps |
| `tornado` [NEW] | Async Loop | High | Medium | High Concurrency/WSGI |
| `gtornado` [NEW] | Greenlet + Async | Very High | High | Extreme Event-driven |

## 💡 Recommendation

- **For Flask/Django**: Start with `gthread` (2-4 workers, 2-4 threads).
- **For FastAPI**: Always use `asgi`.
- **For Tornado Event Loop Integration**: Use `tornado` or `gtornado` for excellent asynchronous connection pooling.
- **For High Concurrency**: Experiment with `gevent` or `gtornado` if your application is compatible.
