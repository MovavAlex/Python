n = int(input())
count = 0
for i in range(n):
    a = input()
    d = a.split()
    if int(d[0]) + int(d[1]) + int(d[2]) >= 2:
        count += 1

print(count)