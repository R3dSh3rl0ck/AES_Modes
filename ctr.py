from Crypto.Cipher import AES
from base64 import *
from Crypto.Util import Counter
plaintext = input('[+] Insert the plaintext : ')
plainbytes = bytes(plaintext, 'utf-8')
key = '16randombytes123'   # change this if you want. (16 bytes) tip -> 1 char = 1 byte
print(f'\nKey value : {key}')
nonce = 'byte'    # change this if you want. (4 bytes)
print(f'\nNonce value : {nonce}')
ctr = Counter.new(64, prefix=nonce, suffix=b'ABCD', little_endian=True, initial_value=10)
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
ct = cipher.encrypt(plainbytes)
print(f'\nThe ciphertext in bytes : {ct}')
print(f'\nThe ciphertext in base64 : {b64encode(ct).decode("utf-8")} \n')
ctr2 = Counter.new(64, prefix=nonce, suffix=b'ABCD', little_endian=True, initial_value=10)
decipher = AES.new(key, AES.MODE_CTR, counter=ctr2)
pt = decipher.decrypt(ct)
readable = pt.decode('utf-8')
print(f'The plaintext after decryption in bytes : {pt}\n')
print(f'The plaintext after decryption : {readable}\n')