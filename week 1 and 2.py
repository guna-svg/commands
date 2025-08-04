# inductation error
"""x = int(input("enter the value: "))
if x > 3:
 print("x is greater than 3")"""
# compound intrest
"""P = int(input("enter the principal account"))      
r = float(input("enter the rate in 5%"))             
n = int(input("enter the times applied per year"))                
t = int(input("enter the No of years "))               
A = P * (1 + r/n)**(n*t)
print("Total amount after {t} years:",A)
ci=A-P
print("compound interest:",ci)"""
#distance between two points
"""import math 
x1 = int(input("Enter x-coordinate of first point: "))
y1 = int(input("Enter y-coordinate of first point: "))
x2 = int(input("Enter x-coordinate of second point: "))
y2 = int(input("Enter y-coordinate of second point: "))
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance between points:",distance)"""
#person details
"""name = input("Enter your Name: ")
email= input("Enter your Email: ")
address= input("Enter your Address: ")
number=int(input("enter Phone Number :"))

print("\nPerson Details:")
print(f"Name: {name}")
print(f"Email: {email}")
print(f"Adress: {address}")
print(f"Phone Number: {number}")"""
#positive difference of two numbers
"""a = int(input("enter the first value: "))
b = int(input("enter the second value: "))

if a > b:
    diff = a - b
else:
    diff = b - a
    
print("The positive difference is:", diff)"""
#check wheather a number is +ve or -ve or zero
"""x=int(input("enter the value: "))
if x>0:
      print("positive number.")
elif x<0:
    print("negative number. ")
else:
    print("neither +ve nor -ve. ZERO",x)"""
#check wheather the given input is digit (or) lowercase character (or) uppercase character (or)special character
x= input("Enter a single character: ")
if x.isdigit():
    print("The input is a digit.")
elif x.islower():
    print("The input is a lowercase character.")
elif x.isupper():
    print("The input is a uppercase character.")
else:
    print("The input is a special character.")
