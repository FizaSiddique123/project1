/**
 * ============================================================================
 * CLINICAL TRIAGE AI - FRONTEND APPLICATION SERVER (PORT 3000)
 * Autonomous Clinical Decision Support System & Symptom Triage Platform
 * ============================================================================
 */

const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

const PORT = 3000;
const HOST = '127.0.0.1';
const ROOT_DIR = __dirname;
const BACKEND_URL = 'http://127.0.0.1:8000';

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.pdf': 'application/pdf',
  '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
  '.txt': 'text/plain; charset=utf-8'
};

const server = http.createServer((req, res) => {
  // CORS Headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  const parsedUrl = url.parse(req.url);
  let pathname = decodeURIComponent(parsedUrl.pathname);

  // Default to index.html
  if (pathname === '/' || pathname === '') {
    pathname = '/index.html';
  }

  // Optional reverse proxy for /api to avoid any CORS complications
  if (pathname.startsWith('/api/')) {
    const proxyReq = http.request(
      `${BACKEND_URL}${req.url}`,
      {
        method: req.method,
        headers: {
          ...req.headers,
          host: '127.0.0.1:8000'
        }
      },
      (proxyRes) => {
        res.writeHead(proxyRes.statusCode, proxyRes.headers);
        proxyRes.pipe(res);
      }
    );

    proxyReq.on('error', (err) => {
      console.error(`[Proxy Error] ${req.method} ${pathname}:`, err.message);
      res.writeHead(502, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({
        success: false,
        error: "Backend API is currently offline. Please ensure Python backend is running on port 8000."
      }));
    });

    req.pipe(proxyReq);
    return;
  }

  // Resolve file path safely
  let filePath = path.join(ROOT_DIR, pathname);
  
  // Prevent directory traversal
  if (!filePath.startsWith(ROOT_DIR)) {
    res.writeHead(403, { 'Content-Type': 'text/plain' });
    res.end('403 Forbidden');
    return;
  }

  fs.stat(filePath, (err, stats) => {
    if (err || !stats.isFile()) {
      // If file not found, fallback to index.html for SPA client routing
      filePath = path.join(ROOT_DIR, 'index.html');
    }

    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';

    fs.readFile(filePath, (readErr, content) => {
      if (readErr) {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end('500 Internal Server Error');
        return;
      }

      res.writeHead(200, {
        'Content-Type': contentType,
        'Cache-Control': 'no-cache, no-store, must-revalidate'
      });
      res.end(content);
    });
  });
});

server.listen(PORT, HOST, () => {
  console.log('====================================================================');
  console.log('🏥 CLINICAL TRIAGE AI — FRONTEND APPLICATION SERVER ONLINE');
  console.log(`👉 USER-FACING APPLICATION: http://${HOST}:${PORT}`);
  console.log(`🔗 CONNECTED BACKEND REST API: ${BACKEND_URL}`);
  console.log('Autonomous Clinical Decision Support System • Enterprise Triage Engine');
  console.log('====================================================================');
});
