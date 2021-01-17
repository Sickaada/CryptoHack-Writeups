from pwn import *  # pip install pwntools
import json
import codecs
import base64
from Crypto.Util.number import bytes_to_long, long_to_bytes

# connecting with remote server
r = remote('socket.cryptohack.org', 13377, level='debug')


def decoding(received):
    if typeof == "base64":
        decoded = base64.b64decode(encoded).decode('UTF-8')
    elif typeof == "hex":
        decoded = bytes.fromhex(encoded).decode('UTF-8')
    elif typeof == "rot13":
        decoded = codecs.decode(encoded, 'rot_13')
    elif typeof == "bigint":
        len_dec = len(encoded)
        decoded = int(encoded, 16).to_bytes(
            len_dec, 'big').decode('UTF-8').replace('\x00', '')
    elif typeof == "utf-8":
        decoded = ""
        for i in encoded:
            decoded += chr(i)
    return decoded


for i in range(101):
    def json_recv():
        line = r.recvline()

        return json.loads(line.decode())

    def json_send(hsh):
        request = json.dumps(hsh).encode()
        r.sendline(request)

    received = json_recv()

    typeof = received["type"]

    encoded = received["encoded"]

    to_send = {
        "decoded": decoding(received)
    }
    json_send(to_send)
    print(i)
