#!/bin/sh
INSTANCE=${SERVER_INSTANCE:-1}

if [ "$INSTANCE" = "2" ]; then
  COLOR="background:#10b981"
else
  COLOR="background:#3b82f6"
fi

# Match <body ...> với bất kỳ attributes nào
sed -i "s|<body\([^>]*\)>|<body\1><div style='${COLOR};color:#fff;text-align:center;padding:8px;font-family:sans-serif;font-weight:bold;position:fixed;top:0;width:100%;z-index:9999;'>🌐 Web Frontend Server — Instance #${INSTANCE}</div>|" /usr/share/nginx/html/index.html

nginx -g "daemon off;"