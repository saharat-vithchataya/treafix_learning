import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler


# Define the HTTP request handler class
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Handle GET requests
    def do_GET(self):
        # Set response status code
        self.send_response(200)

        # Set headers
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # HTML response content
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Simple Python Web Server</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is a simple Python web server running on port {self.server.server_port}.</p>
        </body>
        </html>
        """

        # Write HTML content to response
        self.wfile.write(html_content.encode("utf-8"))


def run_server(port):
    # Define server address
    server_address = ("", port)

    # Create an HTTP server instance
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

    # Start the server
    print(f"Server running on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    # Create argument parser
    parser = argparse.ArgumentParser(description="Simple Python Web Server")

    # Add argument for port
    parser.add_argument(
        "--port", type=int, default=8000, help="Port to run the server on"
    )

    # Parse arguments
    args = parser.parse_args()

    # Run the server
    run_server(args.port)
