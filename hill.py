import numpy as np
import re
import math


class HillCipher:
    def __init__(self, key_matrix):
        self.key_matrix = np.array(key_matrix, dtype=int)
        self.n = len(key_matrix)
        
        if self.key_matrix.shape != (self.n, self.n):
            raise ValueError("Ключевая матрица должна быть квадратной")
        
        det = int(np.linalg.det(self.key_matrix)) % 26
        if math.gcd(det, 26) != 1:
            raise ValueError("Определитель матрицы должен быть взаимно прост с 26")
    
    def _text_to_numbers(self, text):
        return [ord(char) - ord('A') for char in text]
    
    def _numbers_to_text(self, numbers):
        return ''.join([chr(num + ord('A')) for num in numbers])
    
    def _prepare_text(self, text):
        prepared = re.sub(r'[^A-Za-z]', '', text.upper())
        
        while len(prepared) % self.n != 0:
            prepared += 'X' 
        
        return prepared
    
    def encrypt(self, plaintext):
        prepared_text = self._prepare_text(plaintext)
        
        numbers = self._text_to_numbers(prepared_text)
        
        blocks = [numbers[i:i + self.n] for i in range(0, len(numbers), self.n)]
        
        encrypted_blocks = []
        
        for block in blocks:
            encrypted_block = np.dot(self.key_matrix, block) % 26
            encrypted_blocks.extend(encrypted_block)
        
        return self._numbers_to_text(encrypted_blocks)
    


def main():
    print("пример с матрицей 2x2:")
    key_2x2 = [[3, 3], [2, 5]]
    hill_cipher_2x2 = HillCipher(key_2x2)
    
    plaintext = "HELLO WORLD"
    print(f"исходный текст: {plaintext}")
    
    encrypted = hill_cipher_2x2.encrypt(plaintext)
    print(f"зашифрованный текст: {encrypted}")
    print()
    
    print("пример с матрицей 3x3:")
    key_3x3 = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
    hill_cipher_3x3 = HillCipher(key_3x3)
    
    plaintext_3x3 = "CRYPTOGRAPHY"
    print(f"исходный текст: {plaintext_3x3}")
    
    encrypted_3x3 = hill_cipher_3x3.encrypt(plaintext_3x3)
    print(f"зашифрованный текст: {encrypted_3x3}")
    print()
    
    text = input("текст для шифрования: ")
    matrix_size = input("размер матрицы (2 / 3): ").strip()
    
    try:
        if matrix_size == '2':
            key = [[3, 3], [2, 5]]
            cipher = HillCipher(key)
        elif matrix_size == '3':
            key = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
            cipher = HillCipher(key)
        else:
            print("неверный размер матрицы")
        
        encrypted = cipher.encrypt(text)
        print(f"зашифрованный текст: {encrypted}")
        
    except Exception as e:
        print(f"ошибка: {e}")


if __name__ == "__main__":
    main()
