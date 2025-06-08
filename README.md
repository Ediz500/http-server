# Basic HTTP Server (Socket + Docker + Compose)

This is a minimal HTTP server implemented in Python using raw sockets and threading, without using any frameworks.

## 🔧 Features

- Handles basic `GET` requests
- Serves static files from `/static` directory
- Responds with JSON from `/api/hello`
- Correct `Content-Type` (MIME) handling
- Multithreading for handling multiple clients
- 404 and 500 error handling

## 🐳 Docker Support

You can run this server using Docker:

```bash
docker build -t http-server .
docker run -p 8080:8080 http-server
```

Or with Docker Compose:

```bash
docker compose up --build
```
