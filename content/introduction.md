# 🌟 Introduction

**Asteri** is a high-performance, production-ready Python web server designed for modern developer workflows. It bridges the gap between traditional WSGI servers like Gunicorn and modern ASGI servers like Uvicorn, offering a unified, rich CLI and configuration system for any Python web application.

## 🚀 Why Asteri?

In the current Python ecosystem, developers often have to switch between different servers depending on their framework (Flask vs FastAPI) or concurrency model (Sync vs Async). Asteri eliminates this friction by providing a singular, robust platform that handles multiple protocols with ease. Whether you are building a legacy enterprise application or a cutting-edge asynchronous API, Asteri provides the tools to ensure maximum stability and speed.

Asteri is not just a server; it's a complete runtime environment for Python web applications. It focuses on:
- **Unified Interface**: Use the same CLI arguments for WSGI, ASGI, and even uWSGI.
- **Superior Concurrency**: Built-in support for multiple worker models including Gevent (greenlets) and Gthreads.
- **Protocol Auto-Detection**: Asteri can automatically detect the protocol required by your application or environment.
- **Native Observability**: A premium, built-in status dashboard that provides real-time metrics without external dependencies.

## 🏛️ Architecture Overview

At its core, Asteri uses a **Master-Worker process model**. The Master process (Arbiter) is responsible for managing the lifecycle of worker processes. It handles signals, manages configurations, and ensures that the requested number of workers are always running.

The workers themselves are where the application logic lives. By separating the management logic from the request handling, Asteri ensures that a single crashing worker won't bring down the entire server. This architecture is battle-tested and provides the reliability needed for high-traffic production environments.

## ✨ Key Features

- **Multi-Protocol Support**: Full implementation of HTTP/1.1 and HTTP/2. Native support for WSGI, ASGI, and binary uWSGI.
- **Worker Diversity**:
  - `sync`: Best for short-lived, CPU-bound requests.
  - `gthread`: Ideal for I/O-bound requests with thread-safe applications.
  - `gevent`: Extremely high performance for massive concurrency using non-blocking I/O.
  - `asgi`: Optimized for modern asynchronous frameworks like FastAPI and Starlette.
- **Reliability**: Advanced process management with master-worker architecture, graceful timeouts, and automatic worker recycling (max-requests).
- **Security First**: Easy SSL/TLS integration and support for running workers under restricted users/groups.
- **Developer Experience**: Professional-grade logging, live-reloading, and an intuitive CLI.

## 🎯 Our Mission

The mission of the Asteri project is to simplify Python web deployment. We believe that developers should spend more time writing code and less time wrestling with server configurations. By providing a "batteries-included" server that works out of the box with any framework, we aim to become the standard choice for the next generation of Python developers.

## 📊 Performance Benchmark

Asteri is engineered for efficiency. In high-concurrency scenarios, it consistently matches or outperforms industry standards.

| Server Name | Protocol | RPS (Requests Per Second) | Latency (ms) |
|-------------|----------|---------------------------|--------------|
| **Asteri (Sync)** | WSGI | **23.71** | **2108.39** |
| **Asteri (ASGI)** | ASGI | **23.47** | **2130.29** |
| Asteri (Gevent) | WSGI | 22.84 | 2189.49 |
| Uvicorn | ASGI | 22.73 | 2199.27 |
| Gunicorn (Sync) | WSGI | 22.06 | 2266.41 |

*Note: Benchmarks vary based on environment. Tested with 1000 requests at 50 concurrent connections.*
