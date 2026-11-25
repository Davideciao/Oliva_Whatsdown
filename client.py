import socket
import threading

HOST = '127.0.0.1'
PORT = 676767

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
    s.connect( (HOST, PORT) )

    # avvio il thread --> mi consente di ricevere più messaggi contemporaneamente
    threading.Thread( target=ricevi messaggio, args=(), daemon=True ).start()