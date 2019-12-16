import math
def findCoords(path):
    xi = 0
    yi = 0
    coords = []
    for p in path.split(','):
        #print(p)
        x = xi
        y = yi
        if p[0] == 'R':
            x = x + int(p[1:])

            for a in range(xi, x):
                coords.append((a, y))
        if p[0] == 'L':
            x = x - int(p[1:])
            for a in range(xi, x,-1):
                coords.append((a, y))
        if p[0] == 'U':
            y = y + int(p[1:])
            for a in range(yi,y):
                coords.append((x,a))
        if p[0] == 'D':
            y = y - int(p[1:])
            for a in range(yi,y,-1):
                coords.append((x,a))
        xi = x
        yi = y
    return coords


file = open('Input3.txt','r')
i = 0
path = ['','']
coords = []
for line in file:
    path[i] = line
    coords.append(findCoords(path[i]))
    i = i + 1
#print(coords[0])
#print(coords[1])
min_dis = 1000
min_point = (0,0)
crosspaths = []
path1 = 0
min_path = 100000
for i in range(0,len(coords[0])):
    x,y = coords[0][i]
    for j in range(0,len(coords[1])):
        a, b = coords[1][j]
        if x==a and b==y:
            crosspaths.append((x,y))
            if x != 0 and y!= 0:
                dis = math.fabs(x) + math.fabs(y)
                if dis < min_dis:
                    min_dis = dis
                    min_point = (x, y)
                if (i+j)<min_path:
                    min_path = i + j

print(crosspaths)
print((min_point,min_dis))
print(min_path)