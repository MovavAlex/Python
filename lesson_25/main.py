from random import randint
# class Human:
#     location = 'novosibirsk'# public static
#     #__location = 'omsk' # private static
#
#     def __init__(self, rost=1, ves=2):
#         self.height = rost #public dynamic
#         self.__weight = ves # private dynamic
#         self.wfrom = Human.location #использование статики
#
#     def __private(self):
#         pass
#     def public(self):
#         pass
#
# man = Human(10)
# print(man.height)
# print(man.wfrom)





class Human:
    default_name = 'Anton'
    default_age = 100
    def __init__(self,name = 'Oleg', age= 21, money=1, house='Романова'):
        self.Hn = name
        self.Ha = age
        self.__Hm = money
        self.__Hh = house
    def info(self):
        print(self.Hn)
        print(self.Ha)
        print(self.__Hm)
        print(self.__Hh)

    def earn_money(self, new):
        if self.__Hm <= new:
            self.__money = self.__Hm + new
            return self.__money

    def default_info(self):
        print(Human.default_name)
        print(Human.default_age)


    def __make_deal(self, dom):
        if self.__Hm >= dom.final_price(): #если хватает -> тратим
            self.__Hm -= dom.final_price()
            return True
        else:
            return False

    def buy_house(self, dom):
        if self.__make_deal(dom):
            dom.owner = self.Hn
            self.__Hh = dom
            return 'Дом куплен'
        else:
            return f'Денег не хватило, нужно еще: {dom.final_price()-self.__Hm}'

man = Human('Oleg', 21, 1000, 'Романова')


class House:
    def __init__(self, area='nsk', price=20000):
        self.__price = price
        self.__area = area
        self.__sale = randint(5,25)

    def final_price(self):
            return self.__price - self.__price* (self.__sale / 100)


dom = House()




man.buy_house(dom)
print(man.buy_house(dom))
