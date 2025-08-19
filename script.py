new_phrase = ""
decrypted_phrase = ""

def choice():
    option = str(input("Type 1 for Encrypt, 2 for Decrypt: "))
    if(option == "1"):
        #encrypt phase
        phraseinput()
        encrypt()
    elif(option == "2"):
        #decrypt phase
        decrypt()
    else:
        print("You input an invalid option, try again!")
        choice()


def phraseinput():
    try:
        global phrase
        phrase = str(input("Input phrase to encrypt: "))
        print(phrase)
        shiftinput()
    except:
        print("Enter a valid phrase (only letters)")

def shiftinput():
    try:
        global shift
        shift = (int(input("Input shift amount: ")))%26
        print(shift)
    except:
        print("Enter a number only")
        shiftinput()

def encrypt():
    for x in phrase:
        if(x==" "):
            newletter = ord(x)
        else:
            if((ord(x)+shift)>122):
                difference = 122 - ord(x)
                new = shift - difference
                wrapped = 96 + new
                newletter = wrapped
            else:
                newletter = ord(x) + shift

        global new_phrase
        new_phrase += chr(newletter)
    print(new_phrase)


def decrypt():
    try:
        global decryptphrase
        decryptphrase = str(input("Input phrase to Decrypt: "))
        print(decryptphrase)
        shiftdecrypt()
    except:
        print("Enter a valid phrase (only letters)")
        decrypt()
    

def shiftdecrypt():
    try:
        global shiftdecryptnumber
        shiftdecryptnumber = (int(input("Do you know the shift number? If so type it here: ")))%26
        print(shiftdecryptnumber)
        decryption()
    except:
        print("Enter a number only")
        shiftdecrypt()

def decryption():
    for x in decryptphrase:
        if(x==" "):
            decryptedletter = ord(x)
        else:
            decryptedletter = ord(x) - shiftdecryptnumber
        global decrypted_phrase
        decrypted_phrase += chr(decryptedletter)
    print(decrypted_phrase)
    correct = str(input("Does this phrase look correct? Type either yes or no (Case Sensitive)"))
    if(correct == "yes"):
        print("Hooray phrase decrypted!")
    elif(correct == "no"):
        print("Lets try more shift keys!")
        shiftguesser()
    else:
        print("Enter either yes or no")
        

def shiftguesser():
    print("lets do this")
    phrase = "olssv ibbkf ovc hyl fvb avkhf"
    with open("wordlist.txt") as f:
        words = [line.strip() for line in f]
    i = 0
    
    while i < 26:
        decrypted_phrase = ""
        for x in phrase:
            if(x==" "):
                decryptedletter = ord(x)
                decrypted_phrase += chr(decryptedletter)
            else:
                decryptedletter = ord(x) - i
                decrypted_phrase += chr(decryptedletter)
            
        newarray = decrypted_phrase.split() 
            
        for x in newarray:
            if x in words:
                print("This phrase was shifted by: " + str(i))
                print("Your decrypted phrase is: " + decrypted_phrase)
                break
                
           
        i += 1
            
    
    
        
    
shiftguesser()
#choice()