import time

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a ,b):
    return a*b

def divi(a,b):
    return a//b

def power(a,b):
    return a**b

if __name__ == '__main__' :
    while True:
        print('Simple calculator to perform mathematical operations: ')
        print(' 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Exit')
        choice = int(input('Enter the number to perform the operation :'))
        if choice == 1:
            print('Decimal input can"t be processed !!')
            num1 =int(input('Enter the first number :'))
            num2 =int(input('Enter the second number :'))
            result=add(num1 , num2)
            print(result)
            time.sleep(4)
        elif choice == 2:
            print('Decimal input can"t be processed !!')
            num1 =int(input('Enter the first number :'))
            num2 =int(input('Enter the second number :'))
            result=sub(num1 , num2)
            print(result)
            time.sleep(4)
        elif choice == 3:
            print('Decimal input can"t be processed !!')
            num1 =int(input('Enter the first number :'))
            num2 =int(input('Enter the second number :'))
            result=mult(num1 , num2)
            print(result)
            time.sleep(4)
        elif choice == 4:
            print('Decimal input can"t be processed !!')
            num1 =int(input('Enter the first number :'))
            num2 =int(input('Enter the second number :'))
            result=divi(num1 , num2)
            print(result)
            time.sleep(4)
        elif choice == 5:
            print('We are exiting ......')
            break