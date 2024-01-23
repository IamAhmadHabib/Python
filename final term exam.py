def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % (i + 2) == 0 or n % i == 0 :
            return False
        i += 6
    return True

while True:
    number = int(input("Please enter any number you want: "))
    if is_prime(number):
        print(f"{number} is a prime number -- congrats --.")
        break
    else:
        print(f"{number} is not a prime number--congrats--.")