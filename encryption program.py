print("ENCRYPTION PROGRAM \n")

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars : {chars}")
print(f"key : {key}")

# ENCRYPT

originaltext = input("Enter a message to encrypt : ")
ciphertext = ""

for letter in originaltext:
    index = chars.index(letter)
    ciphertext = ciphertext + key[index]

print("Original message : " , originaltext)
print("Encrypted message : " ,ciphertext)

# DECRYPT

ciphertext = input("Enter a message to decrypt : ")
originaltext = ""

for letter in ciphertext:
    index = key.index(letter)
    originaltext = originaltext + chars[index]

print("Encrypted message : " , ciphertext)
print("Original message : " , originaltext)
