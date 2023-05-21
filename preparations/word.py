s = input()
upc = 0
loc = 0
for i in s:
    if i.isupper() == True:
        upc += 1
    elif i.islower() == True:
        loc += 1

if upc > loc:
    print(s.upper())
elif upc < loc or upc == loc:
    print(s.lower())

