import string
# class Human:
#     def __init__(self,height):
#         self.height = height #public
#         self.__money = 0 #private
#
#
#     def ipotek(self):
#         if self.__money > 50 and self.__normal_height():
#             return True
#         else:
#             return 'Попрошу у людей на Маркса'
#
#     def __normal_height(self):
#         if 100 < self.height < 200:
#             return True
#
#
#
# man = Human('///')
# man._Human__money += 5
#
# print(man.ipotek())



#
# class Car():
#     def __init__(self):
#         self.status = False
#     def on(self):
#         if self.status == False:
#             self.status = True
#             return 'Автомобиль заведен'
#         else:
#             return 'Нельзя'
#
#     def off(self):
#         if self.status == True:
#             self.status = False
# #             return 'Автомобиль заглушен'
# #         else:
# #             return 'Нельзя'
# #
# #     def y(self, year):
# #         self.year = year
# #
# #     def t(self, type):
# #         self.type = type
# #
# #     def c(self, color):
# #         self.color = color
# #
# # mashina = Car()
#
#
# #
# # class Alphabet:
# #     def __init__(self, lang, letters):
# #         self.__lang = lang
# #         self.__letters = string.ascii_lowercase
# #     def print(self):
# #         return self.__letters
# #
# #     def letters_num(self):
# #         return len(self.__letters)
# # a = Alphabet('eng','ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# # print(a.print())
# # print(a.letters_num())
#
# import datetime
# class Watch:
#     def __init__(self):
#         self.__h,self.__m,self.__s= datetime.datetime.now().strftime('%H:%M:%S').split(':')
#         self.__h,self.__m,self.__s = int(self.__h),int(self.__m),int(self.__s)
#     def v(self):
#         return f'{str(self.__h).rjust(2,)}:{self.__m}:{self.__s}'
#     def hour(self):
#         self.__h += 1
#     def min(self):
#         self.__m += 1
#     def sec(self):
#         self.__s += 1
#
# time = Watch()
#
#
#
#
#
#
#
