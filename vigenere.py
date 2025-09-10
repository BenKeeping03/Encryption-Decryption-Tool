def vig_encrypt():
    phrase = str(input("Enter a phrase to encrypt: "))
    key = str(input("Enter a key to encrypt with: "))
    extra = 0
    keyword = ""
    keyword = keyword + key
    while len(keyword) < len(phrase):
        if len(phrase) > len(key):
            extra = len(phrase) - len(keyword) 
            keyword = keyword + key[0:extra]

    print(len(phrase))
    print(len(key))
    print(len(keyword))
    print(keyword)

    rows = 26
    col = 26
    vig_matrix = []
    
    i=0
    y=0
    start = 0
    for i in range(26):
        for y in range(26):
            if (65 <= 65 + y + start <= 90):
                print(chr(65 + y + start), end="")
            else:
                letter = chr((y + start) % 26 + 65)
                print(letter , end="")
        print()
      
        start += 1

            
        


vig_encrypt()