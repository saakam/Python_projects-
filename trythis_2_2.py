# 1부터 100까지의 홀수의 합을 구하시오

i, sum = 0, 0

for i in range (1, 101):
    if (i % 2) == 0:    # 나누어서 나머지가 0이면 짝수
        continue
    else:               # 나누어서 나머지가 1이면 홀수
        sum += i
        print(i, sum)