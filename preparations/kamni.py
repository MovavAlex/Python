a = int(input())
b = list(input())
count = 0
for i in range(a):
    if i+1 == a:
        break
    if b[i] == b[i+1]:
        count += 1
    else:
        continue
print(count)











