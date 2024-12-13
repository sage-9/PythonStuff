import string


def sum(a,b):
    return a+b

def historySaver(a,b):
    file="Calculator History.txt"
    with open(file,'a')as f:
        f.write(f"{str(a)}+{str(b)}={str(a+b)}\n")

def requestInput ():
    InputString=input("Enter a number \n")
    try :
        num=int(InputString)
    except ValueError:
        print("That's not a number\n")
    else:        
        return num
   
def Interface():
    a=0
    b=0
    while not a:
        a=requestInput()
    while not b:
        b=requestInput() 
    historySaver(a,b)  
    return sum(a,b)

def main():   
    answer=input("would you like me to add two numbers(y/n)\n")
    while answer != 'y':
        if(answer=='n'):
            input("Okay, press Anykey to exit")
            return            
        elif(answer!='y'):
            print("That's not an answer")
            answer=input("would you like me to add two numbers(y/n)\n")
            continue
    result=Interface()
    print(f"your answer is {result}")
    main()
    
print("Im a simple Calculator, I add two numbers")

main()        

