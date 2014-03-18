import fscc
import time

if __name__ == '__main__':
    p1 = fscc.Port(0)
    p2 = fscc.Port(1)

    p1.write(b'A')
    time.sleep(1)
    p1.write(b'Hello world!')
    time.sleep(1)
    p1.write(b'Incoming packets')
    time.sleep(1)
    p2.write(b'\x55\x21\33\46\78')
    time.sleep(1)
    p1.write(b'\87\x21\33\46\78')
    time.sleep(1)
    p2.write(b'\21\x21\33\46\78')
    time.sleep(1)
    p2.write(b'\19\x21\33\46\78')
