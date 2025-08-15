new_phrase = ""
def phraseinput():
    try:
        global phrase
        phrase = str(input("Input phrase to encrypt: "))
        print(phrase)
    except:
        print("Enter a valid phrase (only letters)")

def shiftinput():
    try:
        global shift
        shift = int(input("Input shift amount: "))
        print(shift)
    except:
        print("Enter a number only")
        shiftinput()

def encrypt():
    for x in phrase:
        if(x==" "):
            newnumber = ord(x)
        else:
            newnumber = ord(x) + shift
        global new_phrase
        new_phrase += chr(newnumber)
    print(new_phrase)

def decision():
    choice = str(input("Type 1 to Decrypt: "))
    if(choice == 1):
        print("Ready to decrypt")
        decrypt()
    else:
        (print("Thank you for encrypting"))

def decrypt():
    try:
        global phrase
        phrase = str(input("Input phrase to Decrypt: "))
        print(phrase)
    except:
        print("Enter a valid phrase (only letters)")


phraseinput()
shiftinput()
encrypt()
decision()