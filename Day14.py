import math
import os
'''
Good job!
Answer part 2 - 4436981
'''
clear = lambda: os.system('clear')
clear()

counts = {}
heir = []
pool = {}
ore = 0
fuel = 0


def findCount():
    global base
    global counts
    global pool
    global fuel
    csum = 1
    # print(pool)
    for n in range(len(base) - 1, 0, -1):
        layer = base[n]
        for l in layer:
            for eq in eqs:
                if eq[len(eq) - 1] == l:
                    req = math.ceil((counts[l] - pool[l]) / int(eq[len(eq) - 2]))
                    for k in range(0, len(eq) - 3, 2):
                        counts[eq[k + 1]] = counts[eq[k + 1]] + req * int(eq[k])
                    counts[l] = req * int(eq[len(eq) - 2]) - counts[l] + pool[l]
                    # print(counts)
    pool = counts.copy()


def sumCount():
    global counts
    csum = 0
    for v in counts.values():
        csum = csum + v
    return csum - counts['ORE']


def findBasis(eqs, basis):
    global base
    global heir
    # print(basis)
    h = []
    for eq in eqs:
        flag = 1
        # print(eq)
        for k in range(0, len(eq) - 3, 2):
            # print(eq[k+1])
            # print('basis:'+basis[0])
            if eq[k + 1] not in basis:
                # print('Inside')
                flag = 0
                break
        if flag == 1 and eq[len(eq) - 1] not in basis:
            # print(eq)
            h.append(eq[len(eq) - 1])
            # print(heir)
    if not h:
        # print('Done')
        return
    else:
        # print(base)
        heir.extend(h)
        # print(heir)
        base.append(h)
        findBasis(eqs, heir)
    # return base


# global comps = []
base = ['ORE']
fuel_eq = []
file = open('Input14.txt', 'r')
eqs = []
for line in file:
    eq = line.replace(',', '').split('\n')[0].split(' ')
    eqs.append(eq)
basis = ['ORE']
for eq in eqs:
    # comps.append(eq[len(eq)-1])
    counts[eq[len(eq) - 1]] = 0
    pool[eq[len(eq) - 1]] = 0
    if eq[len(eq) - 1] == 'FUEL':
        fuel_eq = eq
counts['ORE'] = 0
# print(comps)
# findIng(eqs,'FUEL',1)
findBasis(eqs, basis)
base = base[0:-1]
# print(base)
ore = 0

# counts['ORE'] = 0
psum = 1
while (ore < 1000000000000):
    for eq in eqs:
        counts[eq[len(eq) - 1]] = 0
    for k in range(0, len(fuel_eq) - 3, 2):
        counts[fuel_eq[k + 1]] = int(fuel_eq[k])

    pool['ORE'] = 0
    counts['ORE'] = 0
    findCount()
    ore = ore + counts['ORE']
    psum = 0
    pool['ORE'] = 0
    fuel = fuel + 1
    for v in pool.values():
        psum = psum + v
    clear()
    print('ORE:' + str(ore))
    print('Fuel:' + str(fuel))
    print('Avg:' + str(fuel / ore))
# print(pool)
# print(fuel)
# print(pool)
'''
eqs = [['12','BHML','3','ORE','7','A'],
      ['2','BHML','31','ORE','4','B']]
basis = ['ORE','BHML']
heir = []
for eq in eqs:
  f = 1
  for k in range(0,4,2):
    if eq[k+1] not in basis:
      f = 0
      print('No')
  if f == 1:
    heir.append(eq[len(eq)-1])
print(heir)'''