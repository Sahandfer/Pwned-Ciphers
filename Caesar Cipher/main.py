import sys

# Encrypt plain text with given key
def encrypt(text, key):
    encryptedText = ""
    for i in range (len(text)):
        # based on values in ASCII 
        decrement = 65 if text[i].isupper() else 97
        encryptedText += chr((ord(text[i])-decrement + key)% 26 + decrement)
    print (encryptedText)

# Decrypt cipher text with given key
def decrypt(cipherText, key):
    decryptedText = ""
    for i in range(len(cipherText)):
        # based on values in ASCII 
        decrement = 65 if cipherText[i].isupper() else 97
        decryptedText += chr((ord(cipherText[i])-decrement - key)% 26 + decrement)
    print('Decrypted with key ', key, ' ==> ', decryptedText)

# Decrypt cipher text with brute force
def decrypt_no_key(cipherText):
    for key in range(0,26):
        decrypt(cipherText, key)

if __name__ == '__main__':
    # to get the arguments passed to the program by the command line
    args= sys.argv
    if (len(args)< 3):
        print("Not enough arguments")
    else:
        funcCode = int(args[1])
        text = args[2]
        key = int(args[3]) if len(args)>3 else 6
        decrypt_no_key(text) if funcCode == 3 else (encrypt(text, key) if funcCode == 1 else decrypt(text, key))