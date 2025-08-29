input_phrase = ""
encrypted_phrase = ""
char_ascii = 0
def choice():
    option = int(input("Choose 1 for Encrypt, 2 for Decrypt: "))
    if option == 1:
        atbash_encrypt()

def atbash_encrypt():
    global encrypted_phrase
    phrase = str(input("Type phrase to input: "))
    for char in phrase:
        char_ascii = ord(char)
        if 65 <= char_ascii <= 90:
            difference = char_ascii - 65
            new_letter = chr(90 - difference) 

        elif 97 <= char_ascii <= 122:
            difference = char_ascii - 97
            new_letter = chr(122 - difference)
            
        else:
            new_letter = char

        encrypted_phrase += new_letter
    print(encrypted_phrase)
        



choice()