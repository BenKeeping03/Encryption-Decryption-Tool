
def vig_encrypt():
    phrase = str(input("Enter a phrase to encrypt: "))
    phrase = phrase.upper()
    key = str(input("Enter a key to encrypt with: "))
    key = key.upper()
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

    
    vig_matrix = []
    
    i=0
    y=0
    start = 0
    
    for i in range(26):
        line = []
        for y in range(26):
            
            if (65 <= 65 + y + start <= 90):
                line.append(chr(65 + y + start)) 
            else:
                letter = chr((y + start) % 26 + 65)
                line.append(letter)
            
        vig_matrix.append(line)
        line = ""
    
      
        start += 1
    print(vig_matrix)


    number = 0
    encrypted_phrase = ""
    for x in keyword:
        
        row_num = (ord(keyword[number])-65)
        col_num = (ord(phrase[number])-65)
        print(row_num)
        print(col_num)
        number = number + 1
        encrypted_phrase = encrypted_phrase + vig_matrix[row_num][col_num]
        

    print(encrypted_phrase)




            
        


vig_encrypt()