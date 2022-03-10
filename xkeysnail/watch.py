import sys
if sys.platform.startswith('freebsd'):
    from os import unlink, makedirs, path
    from socket import socket, AF_UNIX, SOCK_DGRAM
    from fcntl import ioctl
    from termios import FIONREAD
    from array import array
    from json import loads
    from select import select
else:
    from inotify_simple import INotify, flags

socket_path = '/tmp/xkeysnail/xkeysnail.sock'

if sys.platform.startswith('freebsd'):
    class faked_event:
        def __init__(self, name):
            self._name = name
        @property
        def name(self):
            return self._name

class watch:
    if sys.platform.startswith('freebsd'):
        def __init__(self):
            self._path = socket_path
            self._object = socket(AF_UNIX, SOCK_DGRAM)
            makedirs(path.dirname(socket_path), mode=0o700, exist_ok=True)
            try:
                unlink(self._path)
            except FileNotFoundError:
                pass
            self._object.bind(self._path)
            self._fd = self._object.fileno()
        def close(self):
            self._object.close()
            unlink(self._path)
        def read(self):
            buf = array('i', [0])
            ioctl(self._fd, FIONREAD, buf, 1)
            size = buf[0]
            data = loads(self._object.recv(size).decode('utf-8'))
            return [faked_event(data['name'])]

    else:
        def __init__(self):
            self._object = INotify()
            self_object.add_watch("/dev/input", flags.CREATE | flags.ATTRIB)
            self._fd = self._object.fd
        def close(self):
            self._object.close()
        def read(self):
            return self._object.reat()

    @property
    def fd(self):
        return self._fd
