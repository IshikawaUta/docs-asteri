# 🌟 Introduction to Asteri

**Asteri** is a high-performance, production-ready Python web server designed to power modern web applications with speed and reliability. It seamlessly bridges the gap between traditional WSGI servers and modern ASGI frameworks, offering a unified interface for any Python web project. Engineered from the ground up to handle the demands of high-traffic environments, Asteri provides developers with a stable, scalable, and intuitive platform for deploying their Python backends.

## 🚀 Why Choose Asteri?

In the evolving Python ecosystem, developers often juggle multiple servers for different tasks. You might use Gunicorn for your Django apps, Uvicorn for FastAPI, and perhaps even uWSGI for legacy systems. This fragmentation leads to inconsistent configurations and complex deployment pipelines.

Asteri eliminates this complexity by providing a singular, robust platform that handles **WSGI, ASGI, and uWSGI** protocols with zero friction. Whether you are deploying a Flask microservice, a FastAPI application, or a legacy uWSGI project, Asteri is engineered to deliver maximum stability and performance. It is not just another web server; it is a comprehensive deployment tool designed to grow with your application from its first lines of code to global scale.

### Key Pillars of Asteri:

- **Unified Interface**: One set of CLI arguments for all your Python web frameworks. No more learning different flag systems for different servers.
- **Superior Concurrency**: Native support for Sync, GThread, Gevent, ASGI, and Tornado (`tornado`/`gtornado`) worker models, allowing you to choose the best strategy for your specific workload.
- **Protocol Auto-Detection**: Intelligent handling of **HTTP/1.1, HTTP/2, HTTP/3 (QUIC)**, and binary uWSGI on the same port, making migration and multi-protocol support seamless.
- **Built-in Observability**: A premium real-time status dashboard, native Prometheus `/metrics` endpoint, and StatsD integration—all included out of the box.
- **⚡ C-Extension Core**: HTTP and uWSGI parsing powered by a native C-Extension for blazing-fast zero-copy throughput, with seamless Pure-Python fallback.
- **💎 Enterprise Quality**: 100% type-safe codebase enforced by Mypy, 100% PEP-8 compliant via Ruff, and automated PyPI publishing via OIDC Trusted Publishing on GitHub Actions.

## 🏛️ Architecture Overview

At its core, Asteri uses a **Master-Worker process model**, similar to proven technologies like Nginx and Gunicorn, but with modern optimizations for Python's unique execution environment. The Master process, known as the **Arbiter**, is the heart of the server. It is responsible for managing the lifecycle of worker processes, ensuring that the desired state is always maintained.

The Arbiter handles system signals (like `SIGTERM` and `SIGHUP`), manages configuration hot-reloading without downtime, and monitors worker health. If a worker process fails or becomes unresponsive, the Arbiter detects the loss and immediately spawns a new worker to take its place. This self-healing capability is what makes Asteri suitable for critical production workloads where uptime is paramount.

The workers themselves are where the application logic lives. By separating the management logic from the request handling, Asteri ensures that a single crashing worker—perhaps due to a memory leak in the application or a segmentation fault in a C-extension—won't bring down the entire server. This architecture provides the isolation and reliability needed for high-traffic production environments.

## ✨ Key Features in Depth

### Worker Diversity and Optimization

- **`sync` (Synchronous)**: The classic model where each request is handled in its own process. This is the safest model for CPU-bound tasks and non-thread-safe applications.
- **`gthread` (GThreaded)**: Uses threads to handle multiple requests within each worker process. This is highly efficient for I/O-bound tasks while maintaining a smaller memory footprint than the sync model.
- **`gevent` (Gevent/Greenlets)**: Leverages cooperative multitasking via greenlets. This allows a single process to handle thousands of concurrent connections with extremely low overhead, making it the king of performance for real-time applications.
- **`asgi` (Asynchronous)**: Built specifically for Python 3's `async/await` ecosystem. It provides the low-latency performance required by frameworks like FastAPI, Starlette, and Quart.
- **`tornado` / `gtornado` (Tornado Asynchronous)**: Integrates standard Tornado event loops and WSGIContainer setups natively inside child processes. GTornado runs on Greenlets to deliver extreme async performance.

### Advanced Reliability Features

Asteri includes professional-grade features such as:

- **Graceful Timeouts**: Ensuring that long-running requests are handled properly without blocking the server indefinitely.
- **Automatic Recycling**: The `max-requests` feature allows workers to be restarted after a certain number of requests, mitigating potential memory leaks in application code.
- **Pre-loading**: Load your application in the Master process to save memory across workers using Copy-on-Write (CoW) optimizations.

## 🎯 Our Mission and Vision

The mission of the Asteri project is to simplify Python web deployment. We believe that developers should spend more time writing code and less time wrestling with server configurations and infrastructure nuances. 

Our vision is to become the "Standard Bearer" for Python web serving. By providing a "batteries-included" server that works out of the box with any framework, we aim to bridge the gap between development and production. Whether you are a student building your first site or a senior engineer managing thousands of microservices, Asteri is designed to be the only server you will ever need.

## 📊 Performance Benchmark

Asteri is engineered for efficiency. In high-concurrency scenarios, it consistently matches or outperforms industry standards, providing the raw throughput needed for modern web scale.

| Server Name | Protocol | RPS (Requests Per Second) | Latency (ms) |
|-------------|----------|---------------------------|--------------|
| 🌟 **Asteri (GTornado)** | WSGI | **32.60** | **1533.55** |
| 🌟 **Asteri (Tornado)** | WSGI | **32.01** | **1561.90** |
| 🌟 **Asteri (GThread)** | WSGI | **31.94** | **1565.61** |
| 🌟 **Asteri (ASGI)** | ASGI | **30.78** | **1624.66** |
| Asteri (Gevent) | WSGI | 30.73 | 1627.05 |
| Asteri (Sync) | WSGI | 30.65 | 1631.20 |
| Gunicorn (Sync) | WSGI | 30.50 | 1639.27 |
| Uvicorn | ASGI | 23.09 | 2165.76 |

*Note: Benchmarks vary based on environment. Tested with 1000 requests at 50 concurrent connections.*

## 🛣️ The Road Ahead

Asteri v2.2.2 has achieved all previously-stated roadmap goals: native **HTTP/3 (QUIC)** support, **Prometheus & OpenTelemetry** metrics integration, and a **C-Extension core** for maximum throughput. Looking forward, we are committed to even deeper cloud-native integrations, minimizing cold-start times for serverless environments, and expanding multi-platform binary wheels for PyPI. We invite you to join our growing community and help shape the future of Python web infrastructure.
