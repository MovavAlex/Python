n = int(input())
lst = []
count = []
for i in range(n):
    b = input().split()
    lst.append(b)
    count = int(lst[i][i+1]) + int(lst[i+1][i+1]) - int(lst[i+1][i])
print(count)
