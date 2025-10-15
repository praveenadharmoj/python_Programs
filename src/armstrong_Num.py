# Armstrong nuber : a number that is equal to the sum of its own digits, each raised to the power of tha total number of digits 

n = int(input("Enter a Number :"))
sum_cubes = sum(int(dig) ** 3 for dig in str(n)) # finding sum cubes
if n == sum_cubes :
  print("The number {n} is an Armstrong number")
else :
  print("The number {n} is not an Armstrong number")

