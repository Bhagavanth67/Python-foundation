a = int(input("enter the first number :"))
while a == True:
    b = int(input("enter the second number :"))
    opt = input("enter the operation from (+,-,*,/,%) :")
    if opt == "+":
        print(a+b)
    elif opt == "-":
        print(a-b)
    elif opt == "*":
        print(a*b)
    elif opt == "/":
        print(a/b)
    elif opt == "%":
        print(a%b)
    else:
        print(invalid)
    opinion = input("do you want to continue (yes,no) :")
    if opinion.lower() == 'no':
        print("Thank you , the calculation has been ended")
        break
