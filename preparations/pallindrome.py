
class Solution(object):
    def isPalindrome(self, x):
        z = str(x)[::-1]
        if str(x) == z:
            return True
        elif str(x) != z:
            return False
tx = int(input())
n = Solution()
print(n.isPalindrome(tx))