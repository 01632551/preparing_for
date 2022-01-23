num = int(input())
sum = 0
quan = 0
while num != 0:
    if num >= 0 and num % 10 == 0:
        sum += num
        quan += 1
    num = int(input())
middNum = sum / quan
print(middNum)