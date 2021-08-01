terrain = [0,1,0,2,1,0,1,3,2,1,2,1]

total_water = 0
for width in range(2,len(terrain) -1):
    for i in range(len(terrain) - width):
        chunk = terrain[i:i+width+1]
        if all(element < chunk[0] for element in chunk[1:-1]) and all(element < chunk[-1] for element in chunk[1:-1]):
            total_water += (width-1)

print(total_water)