#1) лист компрехеншион, где должны быть такие двнные:
# числа которые делятся на 3 и на 5, в противном случае строка "неизвестно", в диапозоне чисел от 1 до 100

# list_ = [i if i % 3 == 0 and i % 5 == 0 else 'неизвестно' for i in range(1, 101)]
# print(list_)

#1) dct = {'hello': None, 'world': None, 'programmer': None} 
# нужно с помощью компрех вместо нон подставить длиннц строки которая сейчас является ключем 

# dct = {'hello': None, 'world': None, 'programmer': None} 
# dct = {k: len(k) for k in dct.keys()}
# print(dct)

# Нужно создать 3 функции, одна регистрирует пользователя, вторая производит логин третья является менеджером, 
# который хранит в себе список пользователей и при обращении проверяет зарегистрирован ли пользователь, если да, 
# то логинит и выводтоит сообщенние, если нет, то выводит функцию регистрации
# users = {'BK': 'Bzmtvk'}
# def login(name):
#     print(f'User, {name}! Youre log in successfully!')
# def reg(name, password):
#     global users
#     users[name] = password
#     print(f'list of users: {users}')
# def manager():
#     name = input('Введите ваш логин: ')
#     password = input('Введите ваш пароль: ')
#     if name in users:
#         login(name, password)
#     else:
#         print('Youre not registrated!')
#         reg(name, password)
#         print('Youre has been register')
# manager()


# 4)Дана бд, реализовать SRUD, при помощи функций C-Create, R-Read/Retrive, U-Update, D-Delete
db = {'John': 23, 'Jack': 52, 'Alex': 23, 'Tom': 34}
def create():
    global db
    name = input('Введите имя: ')
    age = int(input('Введите возраст: '))
    if name in db:
        print('Пользователь уже существует')
    else:
        db[name] = age
        print('Пользователь успешно добавлен')
        print(f'На данный момент список пользователей такой: {db}')
def read():
    global db
    print(db)
def update():
    global db
    name = input('Введите имя: ')
    new_age = int(input('Введите новый возраст: '))
    if name in db:
        db[name] = new_age
        print(f'На данный момент список пользователей такой: {db}')
def delete():  
    global db
    name = input('Введите имя: ')
    if name in db:
        db.pop(name)
        print(f'На данный момент список пользователей такой: {db}')
    else:
        print("Такого имени нет в списке")
create()
read()
update()
delete()