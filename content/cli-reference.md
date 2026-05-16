# 📖 Asteri CLI Mastery Reference

Asteri's command-line interface is engineered for both power and discoverability. This comprehensive reference guide provides a detailed breakdown of every available argument, enabling you to tune your server for any production workload.

## 🌐 Network Settings

| Argument | Description | Default |
|----------|-------------|---------|
| `-b, --bind` | Address to bind (e.g., `127.0.0.1:8000`). Can be specified multiple times. | `127.0.0.1:8000` |
| `--backlog` | The maximum number of pending connections in the socket queue. | `2048` |
| `--reuse-port` | Enables the `SO_REUSEPORT` flag for better load balancing across workers. | `False` |

## 👷 Worker Configuration

| Argument | Description | Default |
|----------|-------------|---------|
| `-w, --workers` | The number of worker processes for handling requests. | `1` |
| `-k, --worker-class` | The type of workers to run (`sync`, `gthread`, `asgi`, `gevent`). | `sync` |
| `--threads` | Number of threads per worker (only applies to `gthread`). | `1` |
| `--worker-connections` | Maximum simultaneous clients per worker. | `1000` |
| `-t, --timeout` | Workers silent for more than this many seconds are killed and restarted. | `30` |
| `--graceful-timeout` | Timeout for graceful worker shutdown after a reload/stop signal. | `30` |
| `--keep-alive` | The number of seconds to wait for requests on a Keep-Alive connection. | `2` |
| `--max-requests` | Restart a worker after it has processed this many requests (prevents leaks). | `0` (None) |
| `--max-requests-jitter` | Random jitter to add to `max-requests` to prevent simultaneous restarts. | `0` |
| `--preload` | Load the application code before forking worker processes. | `False` |

## 🔒 Security & Identity

| Argument | Description | Default |
|----------|-------------|---------|
| `--certfile` | Path to the SSL certificate file for HTTPS support. | `None` |
| `--keyfile` | Path to the SSL key file for HTTPS support. | `None` |
| `--ca-certs` | Path to the CA certificates file for client verification. | `None` |
| `--ssl-version` | SSL version to use (supports TLSv1, TLSv1.1, TLSv1.2). | `TLSv1.2` |
| `--ciphers` | Custom SSL Cipher suite to use for the connection. | `None` |
| `-u, --user` | Switch worker processes to run as this system user. | `None` |
| `-g, --group` | Switch worker processes to run as this system group. | `None` |
| `-m, --umask` | Set the file mode creation mask for the process. | `0` |

## 📝 Logging & Debugging

| Argument | Description | Default |
|----------|-------------|---------|
| `--log-level` | Set the logging threshold (`debug`, `info`, `warning`, `error`, `critical`). | `info` |
| `--access-logfile` | Path to the file where access logs will be written. | `None` |
| `--error-logfile` | Path to the file where error logs will be written. | `None` |
| `--access-logformat` | Custom format string for access logs. | `None` |
| `--capture-output` | Redirect `stdout` and `stderr` to the error log file. | `False` |
| `--check-config` | Validate the current configuration and exit. | `False` |
| `--print-config` | Display the fully resolved configuration settings and exit. | `False` |

## ⚙️ Process Management

| Argument | Description | Default |
|----------|-------------|---------|
| `-D, --daemon` | Run Asteri in the background as a daemon. | `False` |
| `-p, --pid` | Specify the filename for the PID file. | `None` |
| `-n, --name` | Set a custom process name (useful for process monitoring). | `None` |
| `-e, --env` | Set environment variables (e.g., `NAME=VALUE`). Can be repeated. | `[]` |
| `--reload` | Automatically restart workers when application code changes. | `False` |
| `--chdir` | Change the current working directory before loading the application. | `None` |

## 🚀 HTTP/2 & Limits

| Argument | Description | Default |
|----------|-------------|---------|
| `--http-protocols` | Protocols to support (e.g., `h1,h2` for both HTTP/1 and HTTP/2). | `h1` |
| `--http2-max-concurrent-streams` | Maximum number of concurrent streams for HTTP/2. | `100` |
| `--limit-request-line` | Maximum size of the HTTP request line in bytes. | `4094` |
| `--limit-request-fields` | Maximum number of header fields per request. | `100` |
| `--limit-request-field_size` | Maximum size of a single header field in bytes. | `8190` |
