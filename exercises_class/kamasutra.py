
# Kama Sutra Cipher - Pedro G

import random
import string

def key():
    return list(map(chr, range(65, 91)))

def kamacipher(key, plaintext):
    first_hlf = key[:13]
    second_hlf = key[13:]
    cipher_text = ''
    for i in plaintext:
        if i in first_hlf:
            for j in range(0, len(first_hlf)):
                if i == first_hlf[j]:
                    cipher_text += second_hlf[j]
        elif i in second_hlf:
            for j in range(0, len(second_hlf)):
                if i == second_hlf[j]:
                    cipher_text += first_hlf[j]
    return cipher_text

def main():
    plaintext = str(input("Please enter a string you would like to cipher: ")).upper()
    key = key()
    random.shuffle(key)
    print()

print(kama_sutra_cipher(key, x))
print(key)