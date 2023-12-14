print(10 < 1)
print("Arithemetic Operator's")
a = 10
b = 3
c = a + b
d = a / b
e = a % b
f = a ** b
g = a //b
print(c, d, e, f, g)
print("Relational Operator's")
x = 5
y = 10
print(x < y)
print(x > y)
print(x == y)
print(x != y)
print("Logical Operator's")
a = True
b = False
print(a and b)
print(a or b)
print(not a)
print(not b)
print("Assignment Operator's")
x = 5
print(x)
x += 3 
print(x)
print("Membership Operator's")
x = [23, 44, 45]
print(23 in x)
print(44 in x)
print(57 not in x)
print("Bitwise Operator's :")
x = 5
y = 3
print("Bitwise and :", end=' ')
print(x & y)
print("Bitwise or :", end='')
print(x | y)
print("Bitwise not (x = -x -1):", end='')
print(~x)
print(~y)
print("Exclusive or operator :", end='')
print(x ^ y)
print("Left Shift Operator :")
print(x << 1)
print(y << 1)
print("Right Shift Operator : ")
print(x >> 1)
print(y >> 1)
print("Conditional Statements : ")
num = 23
if num < 0:
    print("Negative number")
elif num > 0:
    print("Positive Number")
else:
    print("Zero")

print("I am Batman") if num == 23 else print("You are not batman")

for i in range(11):
    print(i)

i = 1
while i <= 10:
    print("Value of i in while loop is : ", i)
    i+=1

print("Multiples of 5 : ")
for i in range(5, 51, 5):
    print(i)

print("Functions : ")
def func():
    print("This is a function in python")
def add(num1, num2):#parameter
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2

print(add(23, 23))#here 23, 23 are arguments
print(sub(23, 23))
print(mul(23, 29))

def company(name):
    print("Hello ", name, " Welcome to the class")

company("Chandan")