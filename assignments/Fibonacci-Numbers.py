#This code produces fibonacci series with given length
#For example this is a 10 element fibonacci →  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
length = 10
fibonacci_list = []
for i in range(length):
    if i <= 1:
        fibonacci_list.append(1)
    else:
        next_num = sum(fibonacci_list[i-2:i])
        fibonacci_list.append(next_num)

print(fibonacci_list)