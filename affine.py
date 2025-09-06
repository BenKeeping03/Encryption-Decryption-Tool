char_ascii = 0
encrypted_phrase = ""
decrypted_phrase = ""
def choice():
    option = int(input("Enter 1 to Encrypt, 2 to Decrypt: "))
    if option == 1:
        print("op1")
        affine_encrypt()
    elif option == 2:
        print("op2")
        affine_decrypt()
    else:
        print("Select a valid input (1 or 2)")
        choice()

def affine_encrypt():
    phrase = str(input("Type a phrase to encrypt: "))
    a = int(input("Select a value for A this must have no factors that 26 possesses: "))
    b = int(input("Select a value for B: "))
    global encrypted_phrase
    for char in phrase:
        if ((65 <= ord(char)<=90) or (97 <= ord(char) <= 122)):
            x = ord(char.lower()) - 97
            y = ((a*x) + b)%26
            new_letter = chr(y + 97)
            print(y)
            encrypted_phrase += new_letter
        else:
            encrypted_phrase += char
        
    print(encrypted_phrase)

def affine_decrypt():
    phrase = str(input("Type a phrase to decrypt: "))
    a = int(input("Type the value for A: "))
    b = int(input("Type the value for B: "))
    global decrypted_phrase
    for char in phrase:
        if ((65 <= ord(char)<=90) or (97 <= ord(char) <= 122)):
            x = ord(char.lower()) - 97
            a_inverse = pow(a, -1, 26)
            y = (a_inverse * (x - b))%26
            new_letter = chr(y + 97)
            print(y)
            decrypted_phrase += new_letter
        else:
            decrypted_phrase += char
    print(decrypted_phrase)
        
choice()