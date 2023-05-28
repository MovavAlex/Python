n = int(input())
c = input()
ac = 0
dc = 0
for i in c:
    if i == 'A':
        ac += 1
    elif i == 'D':
        dc += 1
if ac > dc:
    print('Anton')
elif dc > ac:
    print('Danik')
else:
    print('Friendship')