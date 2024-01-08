myInt = 25
myInt2 = 32
myStr = 12
myBool = True
myNone = None
myFloat = 4.5
myComplex = 3 + 5j
myList = [1, 2, 3, 4, 5]
myTuple = ("88", "My Strin", True, 23, None, ("a", "b", "c"))
myDict = {"name": "Mustafa", "rollNo": "E12IP", "age": 23}

print("Type of " + str(myInt) + "is" + str(type(myInt)))
print("Type of " + str(myStr) + "is" + str(type(myStr)))
print("Type of " + str(myBool) + "is" + str(type(myBool)))
print("Type of " + str(myNone) + "is" + str(type(myNone)))
print("Type of " + str(myFloat) + "is" + str(type(myFloat)))
print("Type of " + str(myComplex) + "is" + str(type(myComplex)))
print("Type of " + str(myList) + "is" + str(type(myList)))
print("Type of " + str(myTuple) + "is" + str(type(myTuple)))
print("Type of " + str(myDict) + "is" + str(type(myDict)))


print(1 + 1)  # 2
print(6 * 3)  # 18
print(15 - 6)  # 9
print(15 / 6)  # 2.5
print(15 // 6)  # 2 (Agar ans 2.5 hoga tw 2 dedega like Math.floor in JS)
print(5**2)  # 25
print(8**2)  # 64
print(8 % 2)  # 0





# Basic Calculator using Mathematical Operators 
num1 = int(input("Enter the first number: "))
operator = input("Enter the operator: ")
num2 = int(input("Enter the second number: "))
answer = None

if operator == "+":
  answer = num1 + num2
elif operator == '-':
  answer = num1 - num2
elif operator == '*':
  answer = num1 * num2
elif operator == '/':
  answer = num1 / num2
elif operator == '%':
  answer = num1 % num2

print(num1, operator, num2 , "=", answer)





# Typecasting 