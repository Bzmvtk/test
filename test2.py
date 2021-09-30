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

# # список книг {}
# books = {'Financial': 'Theodor Draiser', 'Rich dad, poor dad': 'Robert Kiyosaki', 'Think and get rich': 'Napoleon Hill'}

# # список читателей {имя: {название книги: автор}}
# {'Alex': {'Financial': 'Theodor Draiser'}}

# # функция, которая выводит инфо о книгах которые есть и о читателях
# На данный момент список читателей такой:
# {'Alex': {'Financial': 'Theodor Draiser'}}
# Список книг такой:
# {'Rich dad, poor dad': 'Robert Kiyosaki', 'Think and get rich': 'Napoleon Hill'}

# # функция, которая регистрирует читателя и выдает книгу
# Какую книгу вы хотите получить? выберите из
#  {'Financial': 'Theodor Draiser', 'Rich dad, poor dad': 'Robert Kiyosaki', 'Think and get rich': 'Napoleon Hill'}
#  Введите только название: Financial
#  Введите ваше имя: Alex
#  Ваша заявка успешно оформлена!

# # функция, которая возвращает книгу
# вы хотите взять книгу или вернуть? ведите "взять" или "вернуть": вернуть
# Введите имя: Alex
# Вы хотите вернуть: {'Financial': 'Theodor Draiser'}? да/нет: да
# Книга успешно возвращена

# # функция менеджер, которая распределяет вызов других функций


books = {'Financial': 'Theodor Draiser', 'Rich dad, poor dad': 'Robert Kiyosaki', 'Think and get rich': 'Napoleon Hill'}
users = {}
def us():
    global books
    global users
    print(f'Список книг такой: {books}')
    print(f'На данный момент список читателей такой: {users}')
    manager()
def reg(name, give):
    global books
    global users
    users[name] = {give: books[give]}
def choice():
    global books
    global users
    give = input(f'Какую книгу вы хотите получить? Выберите из \n {books} \n Введите только название:')
    if give in books:
        name = input(f'Введите ваше имя: ')
        if name in users:
            users[name].update({give: books[give]})    
            books.pop(give)
            print('Ваша заявка успешно оформлена!')
            us()
        else:
            reg(name, give)
            books.pop(give)
            print('Ваша заявка успешно оформлена!')
            us()
def manager():
    global books
    global users
    ch = input('Вы хотите взять книгу или вернуть? Ведите "взять", "вернуть", "отмена" или "инфа": ').lower()
    if ch == 'взять':
        choice()
    elif ch == 'вернуть':
        nam = input('Введите имя: ')
        if nam in users:
            choi = input(f'Ваши книги: {users[nam]}\n Какую книгу вы хотите вернуть?: ')
            inp = users[nam]
            for k, v in inp.items():
                    if k == choi:
                        gog = input('Вы точно хотите вернуть ее? да/нет: ')
                        if gog == 'да':
                            books.update({k:v})
                            inp.pop(choi)
                            us()
                        elif gog == 'нет':
                            print('Ну и че ты тратишь мое время')
                            us()
        else:
            print('Такого пользователя не существует')
            us()
    elif ch == 'отмена':
        users.clear()
        print('На этом пока все, покеда')
    elif ch == 'инфа':
        us()
    else:
        print('Че, самый умный что-ли?')
        manager()
manager()