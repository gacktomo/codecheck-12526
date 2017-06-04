#!/usr/bin/env python3
import sys
import websocket
import socket

def on_message(ws, message):
    try:
        pp(json.loads(message))
    except Exception as e:
        print(e)

def on_error(ws, error):
    print(error)
    
def main(argv):
    print("test")
    """
    url = 'ws://challenge-server.code-check.io/api/websocket/hello'
    sock = socket.create_connection([url,"80"])
    """