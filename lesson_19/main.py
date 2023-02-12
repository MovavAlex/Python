alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
reversealph = alphabet[::-1]

alphabet2 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
reversealph2 = alphabet2[::-1]

symbols = ".,?/|&^%$#@!)(~*"


a = input("Введите сообщение: ")

result = ""

for i in a:
    if i.upper() in alphabet2:
        if i.isupper():
            indx = alphabet2.index(i)
            indx2 = reversealph2[indx]
        else:
            indx = alphabet2.index(i.upper())
            indx2 = reversealph2[indx].lower()
        result += indx2
    elif i.upper() in alphabet:
        if i.isupper():
            indx = alphabet.index(i)
            indx2 = reversealph[indx]
        else:
            indx = alphabet.index(i.upper())
            indx2 = reversealph[indx].lower()
        result += indx2
    elif i not in alphabet:#если не буква
        if i.find(symbols) != 1:
            result += i
print(result)