it = int(input())
x = 0
for i in range(it):
    a = input()
    if a.count("++") == 1:
        x += 1
    if a.count("--") == 1:
        x -= 1

print(x)