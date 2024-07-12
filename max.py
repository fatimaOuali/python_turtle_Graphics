# How do you find the greatest of three 
# numbers entered through keyboard 
# in Python? 

A = int(input("Enter an integer A :"))
B = int(input("Enter an integer B :"))
C = int(input("Enter an integer C :"))
Max = A
if B >= Max : Max = B
if C >= Max : Max = C
print("The maximum is :",Max)