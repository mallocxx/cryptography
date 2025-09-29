alphabet_en = "abcdefghijklmnopqrstuvwxyz"
alphabet_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def caesar_cipher(text, key, mode='encrypt'):
    result = ""
    
    for char in text:
        alphabet = None
        is_upper = False
        
        if char.lower() in alphabet_en:
            alphabet = alphabet_en
            is_upper = char.isupper()
        elif char.lower() in alphabet_ru:
            alphabet = alphabet_ru
            is_upper = char.isupper()
        else:
            result += char
            continue
        
        alphabet_len = len(alphabet)
        effective_key = key % alphabet_len
        
        if mode == 'decrypt':
            effective_key = -effective_key
        
        char_index = alphabet.find(char.lower())
        
        new_index = (char_index + effective_key) % alphabet_len
        
        new_char = alphabet[new_index]
        if is_upper:
            new_char = new_char.upper()
        
        result += new_char
    
    return result

if __name__ == "__main__":
    print("1 - шифрование")
    print("2 - дешифрование")
    
    choice = input("режим (1 / 2): ")
    text = input("текст: ")
    key = int(input("ключ: "))
    
    if choice == "1":
        encrypted = caesar_cipher(text, key, 'encrypt')
        print(f"зашифрованный текст: {encrypted}")
    elif choice == "2":
        decrypted = caesar_cipher(text, key, 'decrypt')
        print(f"расшифрованный текст: {decrypted}")
    else:
        print("выберите 1 или 2")