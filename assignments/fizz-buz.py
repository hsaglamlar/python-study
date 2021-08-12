n = 100
for i in range(1,n+1):
    if not i % 15:
       print("Fizz Buzz")
    elif not i % 5:
        print("Buzz")
    elif not i % 3:
        print("Fizz")
    else:
        print(i)