num = int(input())
quantity = 0
while num != 0:
    if num % 2 == 0 and num % 7 == 0:
        quantity += 1
    num = int(input())
print(quantity)