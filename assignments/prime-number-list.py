number = int(input("Please enter the number to make the prime number list : "))

prime_list = [2]

if number > 2:
    for i in range (3,number+1):
      if all(i%prime for prime in prime_list):
          prime_list.append(i)
elif number < 2:
    prime_list = []
    
print(*prime_list)

