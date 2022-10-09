#alphabet = "АБВГДЕЁДЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

#print(alphabet[::-1]) #Вывод в обратном порядке
#[start:end:stop]

#phrase = "антон"
#print(phrase.upper()) #поднять в верхний регистр
#print(phrase.lower()) #опустить в нижний регистр
#phrase1 = "Я фраза, я карта, я антон"
#print(phrase1[0:1].upper()+phrase1[1:])
#print(phrase1.capitalize())

#surname = input("familia").capitalize()
#name = input("name")
#Otchestvo = input("otchestvo")
#print(f"{surname}, {name[0].upper()}. {Otchestvo[0].upper()}.")
#print(surname, name[0].upper() + "." , Otchestvo[0].upper()+ ".")

#x = input("введите слово плез")

#print(x.lower().count("a")) #кол-во маленьких "a"

#x = input("Введите фразу, раздяляя слова запятой")
#print(x.split(", "))


# phrase = input("Введмте фразу ")
# find = input("Что меняем? ")
# replace = input("На что меняем? ")
#
# print(phrase.replace(find, replace))


#phrase = input("Введмте фразу ")
#a = input("Что меняем?")
#b = input("На что меняем?")
#print(phrase.replace(a, b))


# engalphabet = {
#     " ": " ",
#     "а" : "a",
#     "б" : "b",
#     "в" : "a",
#     "г" : "g",
#     "д" : "d",
#     "е" : "e",
#     "ё" : "yo"
#
#
#
#
#
#
#
# }
# x = input("Введите фразу")
# rus = ""
# for bukva in x:
#     rus = rus + engalphabet[bukva]
# print(rus)
#
#
#

print(rus)
email = input("Введите почту")
print(email.split("@"))
login = email.split("@")[0]
domain = email.split("@")[1]
print("Логин: ", login)
print("Домен: ", domain)


