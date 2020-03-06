import sys

# Encrypt plain text with given key
def encrypt(text, key):
    encryptedText = ""
    for i in range(len(text)):
        keyIndex = i % len(key)
        textDecrement = 65 if text[i].isupper() else 97
        keyDecrement = 65 if key[keyIndex].isupper() else 97
        encryptedText += chr(
            (ord(text[i]) + ord(key[keyIndex]) - (textDecrement + keyDecrement)) % 26
            + textDecrement
        )
    print(encryptedText)


# Decrypt cipher text with given key
def decrypt(cipherText, key):
    decryptedText = ""
    for i in range(len(cipherText)):
        keyIndex = i % len(key)
        cipherDecrement = 65 if cipherText[i].isupper() else 97
        keyDecrement = 65 if key[keyIndex].isupper() else 97
        decryptedText += chr(
            (ord(cipherText[i]) - ord(key[keyIndex]) - (cipherDecrement - keyDecrement))
            % 26
            + cipherDecrement
        )
    print("Decrypted with key ", key, " ==> ", decryptedText)


# Decrypt cipher text with brute force
def decrypt_no_key(cipherText):
    print("Not enough computation power")


if __name__ == "__main__":
    # to get the arguments passed to the program by the command line
    args = sys.argv
    if len(args) < 3:
        print("Not enough arguments")
    else:
        funcCode = int(args[1])
        text = args[2]
        key = int(args[3]) if len(args) > 3 else 6
        decrypt_no_key(text) if funcCode == 3 else (
            encrypt(text, key) if funcCode == 1 else decrypt(text, key)
        )

