a = input().split()
sum = 0
count = 0
cost_b = int(a[0])
money = int(a[1])
kolvo = int(a[2])
for i in range(1, kolvo+1):
    sum += cost_b * 1
if sum - money > 0:
    print(sum - money)
else:
    print(0)
