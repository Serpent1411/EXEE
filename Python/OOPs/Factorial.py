#Factorial
num = int(input("Enter the number: "))

def factorail(x=0):
    if x == 0:
        return 1
    else:
        return x * factorail(x-1)

print(factorail(num))