# Encryption program

import random
import string

chars =" " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
keys  = chars.copy()

random.shuffle(keys)

#ENCRYPT
plain_text = input("Enter the text to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]

# print(f"chars: {chars}")
# print(f"keys : {keys}")
print(f"original  text: {plain_text}")
print(f"encrypted text: {cipher_text}")

#DECRYPT
cipher_text = input("Enter the text to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += chars[index]

# print(f"chars: {chars}")
# print(f"keys : {keys}")
print(f"encrypted text: {cipher_text}")
print(f"original  text: {plain_text}")
