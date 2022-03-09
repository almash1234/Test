# num1=str(input("Number1: "))
# num2= int(input("Number2: "))

# try:
#     print(num1/num2)
# except ZeroDivisionError:
#     print("Делить на ноль нельзя!Иди в школу")


while  True:
    num1=int(input("Num1: "))
    num2=int(input ("Num2: "))
    operation= input('+,-,*, / \n')
    if operation=='+':
        print(num1 + num2) 
    elif operation=='-':
        print(num1-num2)
    elif operation =='*':
        print(num1* num2)
    elif operation =='/':
        try:
            print(num1/num2)
        except ZeroDivisionError:
            print("На ноль делить нельзя")



