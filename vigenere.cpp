#include <iostream>
#include <cmath>
#include <cctype>
using namespace std;

struct vigenere
{
    const string alphabetEn = "abcdefghijklmnopqrstuvwxyz";
    const string alphabetRu = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя";

    string encrypt(string text, string key)
    {
        string result;
        int keyIndex = 0;

        for (int charIndex = 0; charIndex < text.length(); charIndex++)
        {
            string alphabet;
            bool isUpper = false;
            char chr = text[charIndex];

            if (alphabetEn.find(toupper(chr)) != string::npos)
            {
                alphabet = alphabetEn;
                isUpper = isupper(chr);
            }
            else if (alphabetRu.find(toupper(chr)) != string::npos)
            {
                alphabet = alphabetRu;
                isUpper = isupper(chr);
            }
            else 
            {
                result += chr;
                continue;
            }

            int alphabetLength = alphabet.length();
            int keyCharIndex = alphabet.find(tolower(key[keyIndex]));
            keyIndex = (keyIndex + 1) % key.length();

            int charIndexInAlphabet = alphabet.find(tolower(chr));

            int newIndex = (charIndexInAlphabet + keyCharIndex) % alphabetLength;

            char newChar = alphabet[newIndex];
            if (isUpper)
            {
                newChar = toupper(newChar);
            }

            result += newChar;
        }
        return result;
    }

    string decrypt(string text, string key)
    {
        string result;
        int keyIndex = 0;

        for (int charIndex = 0; charIndex < text.length(); charIndex++)
        {
            string alphabet;
            bool isUpper = false;
            char chr = text[charIndex];

            if (alphabetEn.find(toupper(chr)) != string::npos)
            {
                alphabet = alphabetEn;
                isUpper = isupper(chr);
            }
            else if (alphabetRu.find(toupper(chr)) != string::npos)
            {
                alphabet = alphabetRu;
                isUpper = isupper(chr);
            }
            else 
            {
                result += chr;
                continue;
            }

            int alphabetLength = alphabet.length();
            int keyCharIndex = alphabet.find(tolower(key[keyIndex]));
            keyIndex = (keyIndex + 1) % key.length();

            int charIndexInAlphabet = alphabet.find(tolower(chr));

            int newIndex = (charIndexInAlphabet - keyCharIndex + alphabetLength) % alphabetLength;

            char newChar = alphabet[newIndex];
            if (isUpper)
            {
                newChar = toupper(newChar);
            }

            result += newChar;
        }
        return result;
    }

    void test(string text, string key, string expectedResult)
    {
        string encrypted = encrypt(text, key);
        string decrypted = decrypt(encrypted, key);
        
        cout << "Original: " << text << endl;
        cout << "Encrypted: " << encrypted << endl;
        cout << "Decrypted: " << decrypted << endl;
        cout << "Expected: " << expectedResult << endl;
        cout << "Test passed: " << (decrypted == text ? "YES" : "NO") << '\n' << endl;
    }
};


int main()
{
    vigenere cipher;
    
    cipher.test("hello", "key", "rijvs");
    cipher.test("hello world", "key", "rijvs uyvjn");
    cipher.test("HELLO", "KEY", "RIJVS");
    cipher.test("HELLO WORLD", "KEY", "RIJVS UYVJN");
    cipher.test("hello, world!", "key", "rijvs, uyvjn!");
    cipher.test("hello123", "key", "rijvs123");
    cipher.test("a", "b", "b");
    cipher.test("a", "z", "z");
    cipher.test("a b c", "key", "k f a");
    cipher.test("A b C", "Key", "K f A");
    cipher.test("ABCD", "XYZ", "XZBA");
    cipher.test("simple test", "key", "cmkzpc diqd");
    cipher.test("LongTextWithSpaces", "key", "VslqXchxUsxfCtymiq");
    cipher.test("short", "key", "clmbx");
    cipher.test("no punctuation", "key", "xs neradyydmmx");
    cipher.test("special$#@!", "key", "ctcmmyv$#@!");
    cipher.test("cipher", "key", "mmnrip");
    cipher.test("Vigenere", "cipher", "Xqvlrvtm");
    cipher.test("Cipher", "key", "Mmnrip");
    cipher.test("Testing123", "key", "Diqdmlq123");
    cipher.test("abcdef", "longkey", "lppjoj");
    cipher.test("123456", "key", "123456");
    cipher.test("all upper case", "key", "kpj etnov akwc");
    cipher.test("mixOfUpperAndLower", "key", "wmvYjSztcbElnPmgip");
    
    return 0;
}