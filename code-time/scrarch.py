# def find_valid(string_tocheck="{[]}()"):
#     item_list = list(string_tocheck)
#     ends={"{":"}", "(":")", "[":"]"}
#     closed_list = []
#     for item in item_list:
#         if len(closed_list)==0 and ends.get(item):
#             closed_list.append(ends[item])
#             continue

#         if len(closed_list)>0 and item == closed_list[-1] :
#             closed_list.pop()
#         elif ends.get(item):
#             closed_list.append(ends[item])
#         else:
#             return False

#     if len(closed_list)>0:
#         return False
#     else:
#         return True

# print(find_valid("(){}[[()]]"))


# # Function to rotate the matrix
# # 90 degree clockwise
# def rotate90Clockwise(A):
#     N = len(A[0])
#     for i in range(N // 2):
#         for j in range(i, N - i - 1):
#             temp = A[i][j]
#             A[i][j] = A[N - 1 - j][i]
#             A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
#             A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
#             A[j][N - 1 - i] = temp

# # Function to print the matrix
# def printMatrix(A):
#     N = len(A[0])
#     for i in range(N):
#         print(A[i])

# # Driver code
# A = [[1, 2, 3, 4],
#      [5, 6, 7, 8],
#      [9, 10, 11, 12],
#      [13, 14, 15, 16]]
# rotate90Clockwise(A)
# printMatrix(A)

# # This code was contributed
# # by pk_tautolo

# num = 4884
# seed = 1
# check = True
# while check:
#     count = seed
#     step = 0
#     while count < num:
#         count = count + int(str(count)[::-1])
#         step += 1
#         if count == num:
#             check = False
#             break
#     if check : seed += 1

# print(f"seed : {seed} in {step} steps")


# zengin_liste=[]
# for i in range(2,1000):
#     sum = 0
#     for j in range(1,i):
#         if i%j == 0:
#             sum +=j
#     if sum > i and i%2:
#         zengin_liste.append([sum,i])
# print("En küçük zengin tek sayı :", zengin_liste[0][1])


# mukemmel=[]
# for i in range(2,500):
#     sum = 0
#     for j in range(1,i):
#         if i%j == 0:
#             sum +=j
#     if sum == i:
#         mukemmel.append(i)
# print(mukemmel)
# #[6, 28, 496]


# def bounce_ball(h,window,bounce):
#     if not (0<bounce<1) or h <=0 or window >= h:
#         return -1
#     else:
#         result = 0
#         while True:
#             h_next = h * bounce
#             if h > window:
#                 result += 1
#             if h_next> window:
#                 result +=1
#             else:
#                 break
#             h = h_next
#         return result

# print(bounce_ball(3,1.5,0.66))


# list1 = ["Mike", "", "Alice", "Jerry", "", "Tom"]
# list2 = filter(lambda x: x !="",list1)
# print(*list2)


# list1 = [[1,4,5], [4], [46,7,3],[7,3]]
# temp = []
# for item in list1:
#     temp.extend(item)
# print(sum(temp))


# terrain = [0,1,0,2,1,0,1,3,2,1,2,1]

# total_water = 0
# for width in range(2,len(terrain) -1):
#     for i in range(len(terrain) - width):
#         chunk = terrain[i:i+width+1]
#         if all(element < chunk[0] for element in chunk[1:-1]) and all(element < chunk[-1] for element in chunk[1:-1]):
#             total_water += (width-1)

# print(total_water)

# import numpy as np

# aaa = np.arange(30).reshape((5,6))
# aaa2= np.array(aaa)
# print(aaa2.size, aaa2.shape, aaa2.dtype, aaa2.itemsize)
# b= np.concatenate((aaa2,aaa),0)
# print(b)
# c=aaa.
# print(c)


# def subset(liste, k):
#     res = [[]]
#     resa = []
#     for i in liste:
#         for j in res:
#             res = res + [j + [i]]
#             if sum(res[-1]) == k:
#                 if res[-1] not in resa:
#                     resa.append(res[-1])
#     if resa == []:
#         return 'Null'
#     else:
#         return resa # tum sonuclar icin
#        # return resa[-1] tek sonuc icin

# subset([1,3,5,12,15,7,8,23,9], 24)


# with open('code-time/file.txt') as f:
#     N = int(f.readline())
#     res = []
#     for _ in range(N):
#         fun, *attr = f.readline().split()
#         if len(attr) == 2:
#             eval("res." + fun + "(" + attr[0] + "," + attr[1] + ")")
#         elif len(attr) == 1:
#             eval("res." + fun + "(" + attr[0] + ")")
#         elif fun == "print":
#             print(res)
#         else:
#             eval("res." + fun + "()")




# import itertools

# with open('code-time/file.txt') as f:
#     k, m = map(int, f.readline().split())
#     nums = []
#     for _ in range(k):
#         integer_list = map(int, f.readline().split())
#         nums.append(list(integer_list))
#     sum_max = 0
#     for combination in itertools.product(*nums):
#         temp = 0
#         for item in combination:
#             temp += item**2
#         if (temp%m) > sum_max:
#             sum_max = temp%m
    
#     print(sum_max)


# def print_rangoli(size):
#     # your code goes here
#     text = "abcdefghijklmnopqrstuvwxyz"
    
#     for i in range(size):
#         print( "-".join(list(text[size-1:size-1-i:-1])).rjust(size*2- 3,"-") + 
#         "-" + text[size-1-i] + "-" +
#         "-".join(list(text[size-i:size:])).ljust(size*2 -3,"-"))
        
#     for i in range(size-2,-1,-1):
#         print( "-".join(list(text[size-1:size-1-i:-1])).rjust(size*2- 3,"-") + 
#         "-" + text[size-1-i] + "-" +
#         "-".join(list(text[size-i:size:])).ljust(size*2 -3,"-")
#                  )

# if __name__ == '__main__':
#     # n = int(input())
#     print_rangoli(1)



# def merge_the_tools(string, k):
#     # your code goes here
#     for i in range(len(string)//k):
#         print( "".join(set(string[i*k:(i+1)*k])) )

# if __name__ == '__main__':
#     string, k = 'AABCAAADA', 1
#     merge_the_tools(string, k)


# import calendar

# print(calendar.weekday(*[2022,2,25]))
# print(calendar.day_name[4])

# from datetime import datetime

# t1 = datetime.strptime("Sun 10 May 2015 13:54:36 -0700","%a %d %b %Y %H:%M:%S %z")
# print(t1)




# usernames = ["foo","bar","baz"]
# total = []
# for item in usernames:
#     res="NO"
#     for i in range(len(item)-1):
#         a = map(lambda x,y: ord(x) > ord(y), item[i],item[i+1:])
#         print()
#         if bool(list(a)[0]) :
#             res="YES"
#             break
               

#     total.append(res)
        
# print(total)




# dictionary = ['hack', 'a', 'rank', 'khac', 'ackh', 'kran', 'rankhacker', 'a', 'ab', 'ba', 'stairs', 'raits']
# query = ["a", "nark", "bs", "hack", "stair"]

# dict_list = ["".join(sorted(item)) for item in dictionary]

# q_list = ["".join(sorted(item)) for item in query]

# res=dict.fromkeys(q_list,0)
# for q in dict_list:
#     res[q] += 1
# print(res.values)

# from collections import deque

# s=deque([1,2,3,4,5])
# print(type(s[0]))

with open('code-time/file.txt') as f:
    A = set(f.readline().split())
    res="True"  
    for _ in range(int(f.readline())):
        B = set(f.readline().split())
        if not (B.intersection(A)==B and len(A)>len(B)):
            res="False"
    print("False") 