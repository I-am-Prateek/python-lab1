#creating two functions named takeInput() and displayResult()
def takeInput():
        firstnum=int(input("Enter first number:"))
        secondnum=int(input("Enter second number:"))
        operator=input("Enter the operator :")
        displayResult(firstnum,secondnum,operator)
def displayResult(firstnum,secondnum,operator):
    if operator == '+':
        total= firstnum + secondnum
        print(firstnum , "+" , secondnum,"=",total)
    elif operator=='-':
        total= firstnum-secondnum
        print(firstnum,'-',secondnum,"=",total)
    elif operator=='*':
        total= firstnum*secondnum
        print(firstnum,'*',secondnum,"=",total)
    elif operator=='/':
        total= firstnum/secondnum
        print(firstnum,'/',secondnum,"=",total)
    else:
        print("Operator is not correct")

takeInput()
