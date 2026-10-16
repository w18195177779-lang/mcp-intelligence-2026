#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Local Static Site Preview Server
=================================
在本地 8088 端口极速启动静态站预览：
浏览器打开: http://127.0.0.1:8088 即可查看全自动生成的程序化资产站
"""
import http.server
import socketserver
import os
from pathlib import Path

PORT = 8088
DIRECTORY = Path(__file__).resolve().parent

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

print(f"[*] 静态站点预览服务已启动!")
print(f"[*] 浏览器访问地址: http://127.0.0.1:{PORT}")
print(f"[*] 按 Ctrl+C 可停止预览服务。")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] 预览服务已停止。")
