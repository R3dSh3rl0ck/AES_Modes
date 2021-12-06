from Crypto.Cipher import AES
import base64
from Crypto.Util.Padding import pad, unpad
plaintext = input('[+] Insert the plaintext : ')
plainbytes = bytes(plaintext, 'utf-8')
key = '16randombytes123'   # change this if you want.
print(f'\nKey : {key}')
cipher = AES.new(key, AES.MODE_ECB)
ct_bytes = cipher.encrypt(pad(plainbytes, AES.block_size))
print(f'\nThe ciphertext in bytes : {ct_bytes}')
print(f'\nThe ciphertext in base64 : {base64.b64encode(ct_bytes).decode("utf-8")} \n')
pt = unpad(cipher.decrypt(ct_bytes), AES.block_size)
readable = pt.decode('utf-8')
print(f'The plaintext after decryption in bytes : {pt}\n')
print(f'The plaintext after decryption : {readable}\n')