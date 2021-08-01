number = input("Enter a positive integer grater than 1 :")
if not number.isdigit():
    print("It is not a valid number.")
else:
    number = int(number)
    if number == 2:
        print("2 is a prime number.")
    elif number > 2:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is a not prime number.")
    elif number < 2:
        print("Number is expected to be greater than 1")