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


mukemmel=[]
for i in range(2,500):
    sum = 0
    for j in range(1,i):
        if i%j == 0:
            sum +=j
    if sum == i:
        mukemmel.append(i)
print(mukemmel)
#[6, 28, 496]