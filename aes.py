from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

key = os.urandom(16)

cipher = AES.new(key, AES.MODE_ECB)
plaintext = b"HELLO_AES_12345"  
padded = pad(plaintext, 16)  

ciphertext = cipher.encrypt(padded)
print("Шифртекст:", ciphertext.hex())

decipher = AES.new(key, AES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
unpadded = unpad(decrypted, 16)  

print("Расшифровано:", unpadded)
