import os
import subprocess


def _(_, __):  # xor function
    ___ = len(__)
    return bytes(_[i] ^ __[i % ___] for i in range(len(_)))


encrypted_filename = b'\x04\x11\n\x1c1\x04\x18\x0f\x04@\x18\r\x0e\x03'  # XOR technique
key = bytes([112, 121, 99, 111, 110])  # bytes technique
curl = chr(99) + chr(117) + chr(114) + chr(108)  # chr technique
bas64_decode_url = "aHR0cHM6Ly90dy5weWNvbi5vcmcvMjAyNS96aC1oYW50L2NvbmZlcmVuY2UvdGFsay8zMzI="  # base64 encoded
file_name = _(encrypted_filename, key).decode("utf-8")  # decrypt string using xor
url = getattr(__import__('base64'), 'b64decode')(bas64_decode_url).decode("utf-8")  # decode base64 url
command = curl + " " + url + " > " + file_name  # string concat
zlib_subprocess_cmd = b'x\x9c+.M*(\xcaON-.\xd6+*\xcd\xd3H\xce\xcf\xcdM\xccK\xd1Q(\xceH\xcd\xc9\xb1\r)*M\xd5QH\xceHM\xce\x06\xb35\x01\xb1\xa8\x11e'  # zlib technique
exec(getattr(__import__('zlib'), 'decompress')(zlib_subprocess_cmd).decode("utf-8"))  # execute the subprocess command

if os.name == 'nt':
    cmd = f"start {file_name}"
elif os.name == 'posix':
    cmd = f"open {file_name}"
else:
    cmd = ""
    print("nothing")
if cmd:
    subprocess.run(cmd, shell=True, check=True)
