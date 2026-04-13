#!/bin/sh
INSTANCE=${SERVER_INSTANCE:-1}

# Chỉ thêm banner vào đầu index.html gốc, giữ nguyên nội dung
sed -i "s|<body>|<body><div style='background:#3b82f6;color:#fff;text-align:center;padding:8px;font-family:sans-serif;font-weight:bold;'>🌐 Web Frontend Server — Instance #${INSTANCE}</div>|" /usr/share/nginx/html/index.html

nginx -g "daemon off;"