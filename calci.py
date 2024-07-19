#python program for simple calculator
#addition
def add(num1,num2):
    return num1+num2
#fun for subtraction
def sub(num1,num2):
    return num1-num2
#function for multiplication
def multiply(num1,num2):
    return num1*num2
#function for division
def divide(num1,num2):
    return num1/num2
print("please select operation - \n "
      "1.Add\n"\
        "2.Subtract\n"\
        "3.Multiply\n"\
        "4.Divide")
select = int(input("select which operation do u want to perform"))
number_1 = int(input("Enter first number:"))
number_2 = int(input("Enter second number"))
if select == 1:
    print(number_1, "+",number_2, "=",add(number_1,number_2))
elif select == 2:
    print(number_1, "-",number_2, "=",sub(number_1,number_2))
elif select == 3:
    print(number_1, "*",number_2, "=",multiply(number_1,number_2))
elif select == 4:
    print(number_1, "/",number_2, "=",divide(number_1,number_2))
else:
    print("Invalid option")
