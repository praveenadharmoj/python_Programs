# Prime Number : PM is only divisable by 1 and number itself

def prime_chk(num) :
    if num <= 1 :
        return False
    for i in range(2, int(num ** 0.5) + 1) :
        if num % i == 0 :
            return False
        return True
    ans = int(input("Enter a Number to check for Prime :"))
    print(f"The number{ans} is prime : {prime_chk(ans)}")
