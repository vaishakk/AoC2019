obj_counts = {}

def countOrbits(obj):
    global obj_counts
    if obj == 'COM':
        return 1

    file = open('Input6.txt')
    for line in file:
        l = line.split('\n')[0]
        if l[-3:] == obj:
            for o in obj_counts:
                if obj == o:
                    return obj_counts[o] + 1
            obj_counts[obj] = countOrbits(line[0:3])
            return countOrbits(line[0:3])+1

def findPathtoCOM(obj):

    o = obj[:]
    path = []
    while o != 'COM':
        #print(o)
        file = open('Input6.txt')
        for line in file:
            l = line.split('\n')[0]
            #print(l)
            if l[-3:] == o:
                path.append(l[0:3])

                o = l[0:3]
                #print(o)
                break
    return path


#Part 1
obj = ['COM']
obj_heir = [obj]
count = 0
file = open('Input6.txt')
objs = []
for line in file:
    l = line.split('\n')[0]
    objs.append(l[0:3])
file = open('Input6.txt')
for line in file:
    l = line.split('\n')[0]
    if l[-3:] not in objs:
        countOrbits(l[-3:])
for c in obj_counts.values():
    count = count + c
#print(obj_counts)
print('Number of orbits = '+str(count))
###############################
#Part 2
path1 = findPathtoCOM('YOU')
path2 = findPathtoCOM('SAN')
plen = 0
k1 = 0
flag = 0
for obj1 in path1:
    k2 = 0
    k1 = k1 +1
    for obj2 in path2:
        k2 = k2 + 1
        if obj1 == obj2 and flag == 0:
            plen = k1 + k2
            flag = 1

#print(path1)
#print(path2)
print('Number of orbit changes required = '+str(plen-2))
