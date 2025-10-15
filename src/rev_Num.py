num = int(input("Enter a Number :"))
rev_num = 0
while num != 0 :   # loop until num is not 0
    remainder = num % 10 # finding the remainder
    rev_num = rev_num * 10 + remainder
    num //= 10
    print(f"Reverse of a Number is : {rev_num} ")