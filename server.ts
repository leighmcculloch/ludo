import { serve } from "https://deno.land/std@0.208.0/http/server.ts";
import { serveFile } from "https://deno.land/std@0.208.0/http/file_server.ts";

const PORT = 8000;

async function handler(request: Request): Promise<Response> {
  const url = new URL(request.url);
  
  // Serve the index.html file for the root path
  if (url.pathname === "/" || url.pathname === "/index.html") {
    try {
      return await serveFile(request, "./index.html");
    } catch (error) {
      console.error("Error serving file:", error);
      return new Response("File not found", { status: 404 });
    }
  }
  
  // For any other path, return 404
  return new Response("Not found", { status: 404 });
}

console.log(`🎲 Ludo Game Server starting on http://localhost:${PORT}`);
console.log(`📁 Serving index.html from current directory`);
console.log(`🚀 Open http://localhost:${PORT} in your browser to play!`);

await serve(handler, { port: PORT });