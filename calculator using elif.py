num1=int(input("enter number 1"))
num2=int(input("enter number 2"))

print("number 1 is",num1)
print("number 2 is",num2)

choice_user=int(input("enter your choice"))
print("\n1.addition")
print("\n2.subtraction")
print("\n3.division")
print("\n4.multiplication")
print("\n5.square")
print("\n6.cube")
print("\n7.floor division")


if(choice_user==1):
    addition=num1+num2
    print(addition)

elif(choice_user==2):
    subtraction=num1-num2
    print(subtraction)

elif(choice_user==3):
    division=num1/num2
    print(division)

elif(choice_user==4):
    multiplication=num1*num2
    print(multiplication)

elif(choice_user==5):
    square1=pow(num1,2)
    square2=pow(num2,2)

    print(square1)
    print(square2)

elif(choice_user==6):
    cube1=pow(num1,3)
    cube2=pow(num2,3)

    print(cube1)
    print(cube2)

elif(choice_user==7):
   floordivision=num1//num2
   print(floordivision) 

else:
    print("invalid choice")