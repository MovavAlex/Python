from user import User

u1 = User(surname='Смирнов', name='Антон', login='smir-ant',password='12345')
u2 = User()

# print(u1.login)
# print(u2.login)

#
# print(u1.surname)
# print(u2.surname)



users = [u1, u2]
l = input('Введи логин: ')
p = input('Введи пароль: ')



for chelovek in users:
    if chelovek.log_in(l, p):
        print('Авторизация успешна!')
        current = chelovek #сохраняю текщего пользователя
    else:
        print('Неправильный логин или пароль')
