# w = int(input())
# lst = []
#
# for i in range(w):
#     lst += input().split()
#
#
# for i in lst:
#     if len(i) > 10:
#         print(i[0] + str(len(i[0:-2])) + i[-1])
#     elif len(i) <= 10:
#         print(i)


w = int(input())
for i in range(w):
    a = input()
    if len(a) > 10:
        print(a[0] + str(len(a)-2) + a[-1])
    else:
        print(a)