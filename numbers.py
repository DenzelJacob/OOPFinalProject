def is_even(x):
    return x % 2 == 0

def is_odd(x):
    return x % 2 != 0

def is_prime(x):
    for i in range(2,x):
        if x % i == 0:
            
            return False    
    return True

def is_perfect(x):
    factors = []
    for i in range(1,x):
        if x % i == 0:
            factors.append(i)
 
    sum = 0
    for i in factors:
        sum +=i
    if x == sum:
        return True
    return False


def is_abundant(x):
    factors = []
    for i in range(1,x):
        if x % i == 0:
            factors.append(i)
  
    sum = 0
    for i in factors:
        sum +=i
    if x < sum:
        return True
    return False

#helper func

def main_menu():
    print("Main menu\n")
    print("1 - Find all prime numbers within a given range\n\
2 - Find all perfect numbers within a given range\n\
3 - Find all abundant numbers within a given range\n\
4 - Chart all even, odd, prime, perfect and abudant numbers within a given range\n\
5 - Quit\n\
    ")

ask=0
while True:
    main_menu()

    while True:
        try:
            ask = int(input("Your choice: "))
            if ask <= 5 and ask >= 1:
                break
        except ValueError :
            print("I don't understand that ...\n\n")
            main_menu()
        else:
            print("Enter a number 1-5\n")
            main_menu()

    if ask == 5:
        print("\nGoodbye!")
        exit()

    while True:    
        try:
            start = int(input("Enter starting number (positive only): "))
            if start > 0 :
                break
        except ValueError:
            print("Invalid, try again")
        else:
            print("Invalid, try again")
    while True:    
        try:
            end = int(input("Enter ending number (positive only): "))
            if end > start :
                break
        except ValueError:
            print("Invalid, try again")
        else:
            print("Invalid, try again")

    if ask !=4:
        print("#"*14)
    
    if ask ==1:
        for i in range(start, end+1):
            if is_prime(i):
                print(i)

    elif ask == 2:
        for i in range(start, end+1):
            if is_perfect(i):
                print(i)
    elif ask == 3:
        for i in range(start, end+1):
                    if is_abundant(i):
                        print(i)
    elif ask == 4:
        l = []
        for i in range(start, end+1):
            stat = []
            if is_even(i):
                stat.append(True) 
            else: 
                stat.append(False)

            if is_odd(i):
                stat.append(True) 
            else: 
                stat.append(False)
            
            if is_prime(i):
                stat.append(True) 
            else: 
                stat.append(False)

            if is_perfect(i):
                stat.append(True) 
            else: 
                stat.append(False)

            if is_abundant(i):
                stat.append(True) 
            else: 
                stat.append(False)
            l.append(stat)

        print("Number\tEven\tOdd\tPrime\tPerfect\tAbundant")
        for i in range(0,len(l)):
            temp = str(start+i) +"\t"
            for j in range(0,5):
                if l[i][j]:
                    temp += "x\t"
                else:
                    temp+=" \t"
            print(temp)
        
    if ask != 4:
        print("#"*14+"\n")

    #commit test