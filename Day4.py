def splitNum(num):
    digits = []
    num = int(num)
    while(num>0):
        d = num%10
        num = int(num/10)
        digits.append(d)
    return digits
#print(splitNum(123))
count = 0
for pwd in range(165432,707913):
    digits = splitNum(pwd)
    dec_flag = 0
    eq_flag = 0
    db_flag = 0
    run = 1
    runs = []
    for i in range(1,len(digits)):
        if (digits[i-1] - digits[i]) == 0:
            run = run + 1
            if i == len(digits) - 1:
                runs.append(run)
        else:
            runs.append(run)
            run = 1
        if digits[i-1] < digits[i]:

            dec_flag = 1
    min = 1000
    run_flag = 0
    #print(runs)
    for r in runs:
        if r == 2:
            run_flag = 1

    if run_flag == 1 and dec_flag == 0:
        print(pwd)
        count = count + 1

print(count)