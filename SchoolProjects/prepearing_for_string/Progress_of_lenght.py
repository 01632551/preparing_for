s1 = input()
s2 = input()
s3 = input()
if abs(len(s3) - len(s2)) == abs(len(s2) - len(s1)) or abs(len(s3) - len(s1)) == abs(len(s2) - len(s1)) or abs(len(s3) - len(s1)) == abs(len(s3) - len(s2)):
    print('YES')
else:
    print('NO')