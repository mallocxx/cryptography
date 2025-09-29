alphabet = "abcdefghiklmnopqrstuvwxyz"

def j_remove(string):
    string = string.replace("j", "i")
    return string

def make_matrix(key):
    key = key.lower() + alphabet
    matrix = []
    chars = []
    for char in key:
        chars.append(char)
    for char in chars:
        if char not in matrix:
            matrix.append(char)
    return ''.join(matrix)

def formatter(string):
    result = ""
    for char in string:
        if char.lower() not in alphabet:
            continue
        else:
            result += char
    return result

def make_pairs(text):
    i = 0
    while i < len(text) - 1:
        if text[i] == text[i + 1]:
            text = text[:i+1] + 'x' + text[i+1:]
            i += 2  
        else:
            i += 2
    
    if len(text) % 2 != 0:
        text += 'x'
    
    pairs = [list(text[i:i+2]) for i in range(0, len(text), 2)]
    
    return pairs



def playfair_cipher(text, key):
    pairs = make_pairs(text)
    for pair in pairs:
        a_is_upper = pair[0].isupper()
        b_is_upper = pair[1].isupper()
        a = key.find(pair[0].lower())
        b = key.find(pair[1].lower())
        if a == b:
            pair[1] = "x"
        elif a % 5 == b % 5: 
            pair[0] = key[(a + 5) % 25]
            pair[1] = key[(b + 5) % 25]
        elif a // 5 == b // 5:
            pair[0] = key[a + 1 - 5 * int(not((a + 1) % 5))]
            pair[1] = key[b + 1 - 5 * int(not((b + 1) % 5))]
        else:
            pair[0] = key[(a // 5) * 5 + (b % 5)]
            pair[1] = key[(b // 5) * 5 + (a % 5)] 

        if a_is_upper:
            pair[0] = pair[0].upper()
        if b_is_upper:
            pair[1] = pair[1].upper()
    
    return ''.join([item for sublist in pairs for item in sublist])

# if __name__ == "__main__":
#     text = formatter(j_remove(input("текст: ")))
#     key = make_matrix(formatter(j_remove(input("ключ: ").lower())))
#     print(f'зашифрованный текст: {playfair_cipher(formatter(text), make_matrix(formatter(key)))}')

def test(text, key, result):
    correct = playfair_cipher(formatter(text), make_matrix(formatter(key))) == result.lower()
    if not correct:
        print("текст: ", text)
        print("ключ: ", key) 
        print("ожидаемый результат: ", result.lower())
        print("результат:", playfair_cipher(formatter(text), make_matrix(formatter(key))))
        print(correct)
        print("======================")

test("kamil", "key", "ebnlnv")
test("hello", "key", "DBNVMI")
test("playfair", "cipher", "BSDWRBCA")
test("cryptography", "secure", "USXQNPMGDNLV")
test("information", "security", "YLHMEPBYALOW")
test("attack", "defend", "NUUNBL")
test("data", "encryption", "HTIP")
test("message", "key", "LYXAXGDA")
test("block", "cipher", "LSVRLW")
test("algorithm", "secret", "FHBUELSMKZ")
test("communication", "protocol", "PTQVNMSGREDSRQ")