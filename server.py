#!/usr/bin/env python3
"""
Simple HTTP server for serving the Junior Ludo game.
Alternative to the Deno server for environments where Deno is not available.
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

PORT = 8001

class LudoGameHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve index.html for root path
        if self.path == "/" or self.path == "/index.html":
            self.path = "/index.html"
        
        # Call the parent class method to handle the request
        return super().do_GET()

def main():
    # Change to the directory containing the script
    os.chdir(Path(__file__).parent)
    
    # Check if index.html exists
    if not Path("index.html").exists():
        print("Error: index.html not found in current directory")
        sys.exit(1)
    
    with socketserver.TCPServer(("", PORT), LudoGameHandler) as httpd:
        print(f"🎲 Junior Ludo Game Server starting on http://localhost:{PORT}")
        print(f"📁 Serving index.html from {Path.cwd()}")
        print(f"🚀 Open http://localhost:{PORT} in your browser to play!")
        print("Press Ctrl+C to stop the server")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Server stopped")
            sys.exit(0)

if __name__ == "__main__":
    main()