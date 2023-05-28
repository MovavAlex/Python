a = input()
lst = list(a)
count = 0
for i in range(len(a)):
    if lst[i] == '7':
        count += 1
    elif lst[i] == '4':
        count +=1
if count == 7 or count == 4 or count == 47 or count == 74:
    print('YES')
else:
    print('NO')