import codecs
import base64
from Crypto.Util.number import bytes_to_long, long_to_bytes


typeof = input("Type of encoded string: ")
encoded = input("Type the string: ")


def decoding(encoded):
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


print(decoding(encoded))
