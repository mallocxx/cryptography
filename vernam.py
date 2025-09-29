import os

def vernam_encrypt_decrypt(text, key):
    if isinstance(text, bytes):
        byte_text = text
    else:
        byte_text = text.encode('utf-8')
    
    if isinstance(key, bytes):
        byte_key = key
    else:
        byte_key = key.encode('utf-8')

    if len(byte_text) != len(byte_key):
        raise ValueError("длина текста и ключа должны совпадать")

    encrypted_bytes = bytes([b1 ^ b2 for b1, b2 in zip(byte_text, byte_key)])
    return encrypted_bytes

def generate_key(length):
    return os.urandom(length)

message = "Это секретное сообщение"
message_length = len(message.encode('utf-8'))
random_key_bytes = generate_key(message_length)

encrypted_message = vernam_encrypt_decrypt(message, random_key_bytes)
print(f"зашифрованный текст: {encrypted_message}")

decrypted_message = vernam_encrypt_decrypt(encrypted_message, random_key_bytes)
print(f"расшифрованный текст: {decrypted_message.decode('utf-8')}")