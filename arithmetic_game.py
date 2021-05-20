import my_functions as f
import random
num_sub = 0
num_add = 0
num_multi = 0
num_div = 0

correct_sub = 0
correct_add = 0
correct_multi = 0
correct_div = 0

extra_a =0
extra_s =0
extra_d =0
extra_m =0






width = 5
num_prob = 0
drill = False

num_prob = int(input("How many problems would you like to attempt? "))
while True:
    ask = int(input("How wide do you want your digits to be? 5-10: "))
    if ask >=5 and ask <=10:
        width = ask
        break
    print("Enter valid input.")

ask = input("Would you like to activate 'drill' mode? yes or no: ")
if ask == "yes":
    drill = True


counter = 0
#main driver
while counter < num_prob:
    counter +=1
    op_type = f.rand_op()
    
    value1 = f.random_digit()
    value2 = f.random_digit()
    if op_type == "/":
        value2 = f.divisble_digit(value1)

    print("What is .....")

    if op_type == "+":
        f.add_problem(value1,value2,width)
        num_add +=1
    elif op_type == "-":    
        f.sub_problem(value1,value2,width)
        num_sub +=1
    elif op_type == "/":   
        f.div_problem(value1,value2,width)
        num_div+=1
    elif op_type == "*":   
        f.multi_problem(value1,value2,width)
        num_multi +=1
    
   
    if drill:
        while True:
            ask = int(input ("= "))
            if f.check_answer(value1,value2,ask,op_type):
                if op_type == "+":
                    correct_add +=1
                elif op_type == "-":    
                    correct_sub +=1
                elif op_type == "/":     
                    correct_div +=1
                elif op_type == "*":       
                    correct_multi +=1

                print("Correct!\n")
                break
            if op_type == "+":
                extra_a +=1
            elif op_type == "-":

                extra_s +=1
            elif op_type == "/":     
                extra_d +=1
            elif op_type == "*":       
                extra_m +=1
            print("Sorry, that's not correct.")
    else:
        ask = int(input ("= "))
        if f.check_answer(value1,value2,ask,op_type):
            print("Correct!\n")
            if op_type == "+":
                correct_add +=1
            elif op_type == "-":    
                correct_sub +=1
            elif op_type == "/":     
                correct_div +=1
            elif op_type == "*":       
                correct_multi +=1

                pass
        else:
            print("Sorry, that's not correct.\n")

if num_add > 0:
    print("Total addition problems presented:", num_add)
    if drill:
    
        print("# of extra attempts needed:",extra_a)
    else:
        print ("Correct addtition problems: "+ str(correct_add) +" ("+str(correct_add*100/num_add)+"%)")
else :
    print("No addition problems presented")
print()

if num_sub > 0 :
    print("Total subtraction problems presented:", num_sub)
    if drill:
        print("# of extra attempts needed:",extra_s)
    else:
        print ("Correct addtition problems: "+ str(correct_sub) +" ("+str(correct_sub*100/num_sub)+"%)")
else: 
    print("No subtraction problems presented")
print()

if num_multi > 0:
    print("Total multiplication problems presented:", num_multi)
    if drill:
        print("# of extra attempts needed:",extra_m)
    else:
        print ("Correct addtition problems: "+ str(correct_multi) +" ("+str(correct_multi*100/num_multi)+"%)")
else:
    print("No multiplication problems presented")
print()

if num_div > 0:
    print("Total division problems presented:", num_div)
    if drill:
        print("# of extra attempts needed:",extra_d)
    else:
        print ("Correct addtition problems: "+ str(correct_div) +" ("+str(correct_div*100/num_div)+"%)")
else:
    print("No division problems presented")
print()