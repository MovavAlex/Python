class Solution(object):
    def addTwoNumbers(self, l1, l2):
        a = list(reversed(l1))
        b = list(reversed(l2))
        s1 = ''
        s2 = ''
        for i in a:
            s1 += str(i)
        for i in b:
            s2 += str(i)

        l = int(s1)
        n = int(s2)
        sum = l + n
        lst = []
        for i in str(sum):
            lst.append(i)
        res = list(reversed(lst))
        return res








# l1 = input()
# l2 = input()
# n = Solution
# print(n.addTwoNumbers(l1, l2))

# l1 = input().split()
# # print(l1)