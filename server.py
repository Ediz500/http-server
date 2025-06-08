import socket
import threading
import os
import mimetypes
import json

HOST = '0.0.0.0'
PORT = 8080

def handle_client(conn, addr):
    try:
        request = conn.recv(1024).decode('utf-8')
        if not request:
            conn.close()
            return
        
        method, path, *_ = request.split()
        print(f"{addr} - {method} {path}")

        if method != "GET":
            response = b"HTTP/1.1 405 Method Not Allowed\r\n\r\n"
            conn.sendall(response)
            conn.close()
            return

        if path == "/api/hello":
            body = json.dumps({"message": "Hello, world!"})
            headers = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: application/json\r\n"
                f"Content-Length: {len(body)}\r\n\r\n"
            )
            conn.sendall(headers.encode() + body.encode())
        
        elif path.startswith("/static/"):
            file_path = "." + path
            if os.path.exists(file_path):
                with open(file_path, "rb") as f:
                    content = f.read()
                content_type = mimetypes.guess_type(file_path)[0] or "application/octet-stream"
                headers = (
                    "HTTP/1.1 200 OK\r\n"
                    f"Content-Type: {content_type}\r\n"
                    f"Content-Length: {len(content)}\r\n\r\n"
                )
                conn.sendall(headers.encode() + content)
            else:
                conn.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n404 Not Found")
        
        else:
            conn.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n404 Not Found")
    except Exception as e:
        print("Error:", e)
        conn.sendall(b"HTTP/1.1 500 Internal Server Error\r\n\r\n500 Internal Error")
    finally:
        conn.close()

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"Serving HTTP on {HOST}:{PORT} ...")

        while True:
            conn, addr = server_socket.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    run_server()
