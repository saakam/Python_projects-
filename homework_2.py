# 1부터 100까지의 수 중에서 소수(약수가 1과 자기자신)의 합을 구하시오.

i, sum = 0, 0

for i in range (2, 101):
    chk = True
    for div in range (2, i):
        if i % div == 0:
            chk = False
            break
    if chk == True:
        sum += i
#        print(i, end = ' ')            
        print(i, sum)
        
