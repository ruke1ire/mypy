import importlib
import socket
import sys
import io
from threading import Thread

def refresh():
    globals_ = globals().copy()
    for name in globals_:
        if (name[:2] != "__"):
            del globals()[name]

def reload(packname):
    importlib.reload(packname)

def async_run(func, *args, **kwargs):
    '''
    Asynchronously runs a function that returns None.
    '''
    t = Thread(target=func, args=args, kwargs=kwargs)
    t.daemon = True
    t.start()
    return t

_IP     = "127.0.0.1"
_PORT   = 12321
_udp_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

def prext(*args, **kwargs):
    __prev_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    print(*args, **kwargs)
    out = buffer.getvalue()
    out_enc = str.encode(out)
    while len(out_enc) > 512:
        out_enc_pack = out_enc[:512]
        _udp_sock.sendto(out_enc_pack, (_IP, _PORT))
        out_enc = out_enc[512:]
    _udp_sock.sendto(out_enc, (_IP, _PORT))
    buffer.seek(0)
    buffer.truncate(0)
    sys.stdout = __prev_stdout
