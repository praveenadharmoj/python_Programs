# Factorial : product of all positive intergers lessthan or equal to a given non_negative integer n

def factorial(num):
    if num == 0 :
        return 1
    return num * factorial(num -1)
Res = int(input("Enter a Number to find Factorial :"))
print(f"factorail of {Res} is {factorial(Res)}")
