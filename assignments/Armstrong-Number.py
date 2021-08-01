number = input("Please input a positive integer to check whether it is 'n-Armstrong number' or not :").strip()
number_digits = list(number)
if not set(number_digits).issubset(set("0123456789")):
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
else:
    number_len = len(number_digits)
    num_sum = 0
    for i in number_digits:
        num_sum += int(i)**number_len

    if int(number) == num_sum:
        print(number, "is an n-Armstrong number.")
    else:
        print(number, "is not an n-Armstrong number.")