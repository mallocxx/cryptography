import string

def validate_key(key):
    if len(key) != 26:
        raise ValueError("ключ должен содержать ровно 26 символов")
    
    if len(set(key.lower())) != 26:
        raise ValueError("все символы в ключе должны быть уникальными")
    
    if not key.isalpha():
        raise ValueError("ключ должен содержать только буквы")
    
    return True

def create_substitution_table(key):
    alphabet = string.ascii_lowercase
    substitution_table = {}
    
    for i in range(len(alphabet)):
        substitution_table[alphabet[i]] = key[i].lower()
        substitution_table[alphabet[i].upper()] = key[i].upper()
    
    return substitution_table

def encrypt(text, key):
    validate_key(key)
    substitution_table = create_substitution_table(key)
    
    encrypted_text = ""
    for char in text:
        if char in substitution_table:
            encrypted_text += substitution_table[char]
        else:
            encrypted_text += char
    return encrypted_text


if __name__ == "__main__":
    key = "qwertyuiopasdfghjklzxcvbnm"
    message = "Hello, World!"
    
    try:
        encrypted = encrypt(message, key)
        
        print(f"исходный текст: {message}")
        print(f"зашифрованный текст: {encrypted}")
    except ValueError as e:
        print(f"ошибка: {e}")