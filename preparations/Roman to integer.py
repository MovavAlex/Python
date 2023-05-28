# class Solution(object):
#     def romanToInt(self, s):
#         slovar = {'I'==1,"V"==5,"X"==10,"L"==50,"C"==100,"D"==500,"M"== 1000}
#         for i in s:
#             if s[i] == slovar[i]:
#
#
#
#
#
#
#
# s = input().upper()
# n = Solution
# print(n.romanToInt(s))
# count = 0
# crack = 0
# slovar = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
# keys = slovar.keys()
# for i in range(len(s)):
#     if s[i] in keys:
#         count += slovar[s[i]]
#         if 'IV' or 'IX' in s[i+1]:
#             count -= 1
#         if 'XL' or 'XC' in s[i+1]:
#             count -= 10
#         if 'CD' or 'CM' in s[i+1]:
#             count -= 100
#
# #2216
#
# print(count)
