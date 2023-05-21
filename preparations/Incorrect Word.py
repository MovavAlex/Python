a = input()
m = a.split()
x = int(m[0])
b = int(m[1])
m = m[0]



for i in range(b):
    if m[-1] != '0':
        m = str(x-1)
        x -= 1
    elif m[-1] == '0':
        m = str(x//10)
        x = x // 10
print(x)
