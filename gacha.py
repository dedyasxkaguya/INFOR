status = True
i = 0

while(status == True):
    print("Helo, Welcome to star maker, ")
    row = int(input("How many row do you want ? "))
    if(row <= 36):
        elements = ["i","*", "`" , "^" , "?"]
        for index,e in enumerate(elements):
            print(f"{index + 1}. {e}")
        choice = int(input("From 1 to 5, which element would you choose : ")) -1
        
        if(choice <= len(elements)) :
            
            while(i < row):
                print(" " * (row - i) + elements[choice] * (2*i-1))
                i += 1
                
            while(i > 0):
                print(" " * (row - i) + elements[choice] * (2*i-1))
                i -= 1    
            
        else:
            print("You are not following instructions")
            
    else:
        print("The number you entered is too high")
        