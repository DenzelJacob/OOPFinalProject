
import random


def horizontal_line(width,char):
    temp = char * width
    print(temp)

def vertical_line(shift, height, char):
    for i in range (0, height):
        print((shift-1) * " " + char)

def two_vertical_lines(width, height, char):
    for i in range(0,height):
        print(char+ " " * (width-2)+ char)


def number_0(width,char):
    horizontal_line(width, char)
    two_vertical_lines(width,3,char)
    horizontal_line(width,char)

    

def number_1(shift,char):
    vertical_line(shift,5,char)
    

def number_2(width,char):
    horizontal_line(width,char)
    vertical_line(width,1,char)
    horizontal_line(width,char)
    vertical_line(0,1,char)
    horizontal_line(width,char)

   

def number_3(width,char):
    horizontal_line(width,char)
    vertical_line(width,1,char)
    horizontal_line(width,char)
    vertical_line(width,1,char)
    horizontal_line(width,char)

    



def number_4(width,char):
    two_vertical_lines(width,2,char)
    horizontal_line( width, char)
    vertical_line(width,2,char)

    

def number_5(width,char):
    horizontal_line(width,char)
    vertical_line(1,1,char)
    horizontal_line(width,char)
    vertical_line(width,1,char)
    horizontal_line(width,char)

   

def number_6(width,char):
    horizontal_line(width,char)
    vertical_line(1,1,char)
    horizontal_line(width,char)
    two_vertical_lines(width,1,char)
    horizontal_line(width,char)

    


def number_7(width,char):
    horizontal_line(width,char)
    vertical_line(width,4,char)

   

def number_8(width,char):
    horizontal_line(width,char)
    two_vertical_lines(width,1,char)
    horizontal_line(width,char)
    two_vertical_lines(width,1,char)
    horizontal_line(width,char)

    

def number_9(width,char):
    horizontal_line(width,char)
    two_vertical_lines(width,1,char)
    horizontal_line(width,char)
    vertical_line(width,2, char)



def print_number(integer,width,char):
    if integer == 0:
        number_0(width,char)
    elif integer == 1:
        number_1(width,char)
    elif integer == 2:
        number_2(width,char)
    elif integer == 3:
        number_3(width,char)
    elif integer == 4:
        number_4(width,char)
    elif integer == 5:
        number_5(width,char)
    elif integer == 6:
        number_6(width,char)
    elif integer == 7:
        number_7(width,char)
    elif integer == 8:
        number_8(width,char)
    elif integer == 9:
        number_9(width,char)
    print()

def plus (width, char):
    if width %2 !=0:
        vertical_line(width//2 +1,1,char)
        vertical_line(width//2 +1,1,char)
    else:
        print((width//2 -1)* " " + char*2)
        print((width//2 -1)* " " + char*2)

    horizontal_line(width,char)
    
    if width % 2 !=0:
        vertical_line(width//2 +1,1,char)
        vertical_line(width//2 +1,1,char)
    else:
        print((width//2-1) * " " + char*2)
        print((width//2 -1 )* " " + char*2)
    print()

def minus (width,char):

    print("\n" * 2)
    print(char * width)
    print("\n" *3)
    

def divide (width, char):

    for i in range(0,5):
        print ((width - i -1 )* " " + "*")
    print()


def mulitply(width, char):
   
    print("*"+ (width - 2) * " " + char)
    print((width //4 ) * " " + "*"+ (width // 2 -1) * " " + char)
    if width % 2 != 0:
        print( (width // 2) * " " + char)
    else:
        print( (width // 2-1) * " " + char+char)
    print( (width//4)* " " + "*"+ (width //2 -1) * " " + char)
    print( "*"+ (width - 2) * " " + char)
    print()

def check_answer(num1,num2,answer,op):
    if op == "+":
        if num1 + num2 == answer:
            return True
    elif op == "-":
        if num1 - num2 == answer:
            return True

    elif op == "*":
        if num1 * num2 == answer:
            return True
    elif op == "/": 
        if num1 // num2 == answer:
            return True
    return False


##helper functions



# return divisble num
def random_digit():
    return random.randint(0,9)

def divisble_digit(num1):
    
    while True:
        temp = random.randint(1,9)

        if num1 % temp == 0:
            return temp
    

def add_problem(value1,value2,width):
   
    print_number(value1,width,"*")
    plus(width,"*")
    print_number(value2,width,"*")
    

def sub_problem(value1,value2,width):
 
    print_number(value1,width,"*")
    minus(width,"*")
    print_number(value2,width,"*")
    

def div_problem(value1,value2,width):
    
    print_number(value1,width,"*")
    divide(width,"*")
    print_number(value2,width,"*")
   

def multi_problem(value1,value2,width):
    
    print_number(value1,width,"*")
    mulitply(width,"*")
    print_number(value2,width,"*")
    

def rand_op():
    op = ["+","-","/","*"]
    temp = op[random.randint(0,3)]
    return temp

