import math

alphabet_en = "abcdefghijklmnopqrstuvwxyz"
alphabet_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def key_modif(key, text):
    text_len = len(text)
    key_len = len(key)
    if key_len < text_len:
        key += key * math.ceil((text_len - key_len) / key_len)
    key = key[:text_len]
    return key        

def vigenere_cipher(text, key, mode='encrypt'):
    result = ""
    key_index = 0 
    
    for char_ind in range(len(text)):
        alphabet = None
        is_upper = False
        char = text[char_ind]
        
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
        key_char_index = alphabet.find(key[key_index].lower())
        key_index = (key_index + 1) % len(key) 

        if mode == 'decrypt':
            key_char_index = -key_char_index

        char_index = alphabet.find(char.lower())
        
        new_index = (char_index + key_char_index) % alphabet_len
        
        new_char = alphabet[new_index]
        if is_upper:
            new_char = new_char.upper()
        
        result += new_char

    return result

# if __name__ == "__main__":
#     print("1 - шифрование")
#     print("2 - дешифрование")
    
#     choice = input("режим (1 / 2): ")
#     text = input("текст: ")
#     key = input("ключ: ")
    
#     if choice == "1":
#         encrypted = vigenere_cipher(text, key, 'encrypt')
#         print(f"зашифрованный текст: {encrypted}")
#     elif choice == "2":
#         decrypted = vigenere_cipher(text, key, 'decrypt')
#         print(f"расшифрованный текст: {decrypted}")
#     else:
#         print("выберите 1 или 2")

def test(text, key, result):
    correct = vigenere_cipher(text, key, 'encrypt') == result
    if not correct:
        print("текст: ", text)
        print("ключ: ", key) 
        print("ожидаемый результат: ", result)
        print("результат:", vigenere_cipher(text, key, 'encrypt'))
        print(correct)
        print("======================")

test("hello", "key", "rijvs")
test("hello world", "key", "rijvs uyvjn")
test("HELLO", "KEY", "RIJVS")
test("HELLO WORLD", "KEY", "RIJVS UYVJN")
test("hello, world!", "key", "rijvs, uyvjn!")
test("hello123", "key", "rijvs123")
test("a", "b", "b")
test("a", "z", "z")
test("a b c", "key", "k f a")
test("A b C", "Key", "K f A")
test("ABCD", "XYZ", "XZBA")
test("simple test", "key", "cmkzpc diqd")
test("LongTextWithSpaces", "key", "VslqXchxUsxfCtymiq")
test("short", "key", "clmbx")
test("no punctuation", "key", "xs neradyydmmx")
test("special$#@!", "key", "ctcmmyv$#@!")
test("cipher", "key", "mmnrip")
test("Vigenere", "cipher", "Xqvlrvtm")
test("Cipher", "key", "Mmnrip")
test("Testing123", "key", "Diqdmlq123")
test("abcdef", "longkey", "lppjoj")
test("123456", "key", "123456")
test("all upper case", "key", "kpj etnov akwc")
test("mixOfUpperAndLower", "key", "wmvYjSztcbElnPmgip")


