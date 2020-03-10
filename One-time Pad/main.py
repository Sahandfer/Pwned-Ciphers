import sys
import random
import string


def getKey(text):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for i in range(len(text)))


# Encrypt plain text
def encrypt(text):
    encryptedText = ""
    key = getKey(text)

    for i in range(len(text)):
        textDecrement = 65 if text[i].isupper() else 97
        keyDecrement = 65 if key[i].isupper() else 97
        encryptedText += chr(
            (ord(text[i]) + ord(key[i]) - (textDecrement + keyDecrement)) % 26
            + textDecrement
        )

    print("Encrypted with key ", key, " ==> ", encryptedText)


# Decrypt cipher text with given key
def decrypt(cipherText, key):
    decryptedText = ""
    for i in range(len(cipherText)):
        cipherDecrement = 65 if cipherText[i].isupper() else 97
        keyDecrement = 65 if key[i].isupper() else 97
        decryptedText += chr(
            (ord(cipherText[i]) - ord(key[i]) - (cipherDecrement - keyDecrement)) % 26
            + cipherDecrement
        )
    print("Decrypted with key ", key, " ==> ", decryptedText)


if __name__ == "__main__":
    # to get the arguments passed to the program by the command line
    args = sys.argv
    if len(args) < 3:
        print("Not enough arguments")
    else:
        funcCode = int(args[1])
        text = args[2]
        key = args[3] if len(args) > 3 else 6
        encrypt(text) if funcCode == 1 else decrypt(text, key)
