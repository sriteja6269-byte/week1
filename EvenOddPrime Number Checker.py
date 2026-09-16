def check_even_odd(number):
    if number%2==0:
        return "even"
    else:
        return "odd"
def check_prime(number):
    if number<=1:
        return False
    for i in range(2,number):
        if number % i==0:
            return False
    return True
number=int(input("enter number"))
print("this is:",check_even_odd(number))
if check_prime(number):
    print("this is prime number")
else:
    print("this is not a prime number")