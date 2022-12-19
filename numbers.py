import sys

i = int(input("digite o numero "))
numbers = [4, 6, 7, 8, 2, 5, 0]

if i in numbers:
    print("found")
    sys.exit(0)
    
print("not found")
sys.exit(1)
