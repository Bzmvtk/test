# Дан словарь, в котором ключом является имя студента, а значением
# словарь с его оценками по 3 предметам. Замените оценки названием
# предмета, по которому студент имеет высший балл. Например: a = {'John':
# {'history': 90, 'math': 95, 'literature': 91}, 'Rose': {'history': 92, 'math': 96, 'literature':
# 81},
# 'Kelly': {'history': 84, 'math': 85, 'literature': 87}}
# Результат: {'John': 'math', 'Rose': 'math', 'Kelly': 'literature'}

# a = {'John': {'history': 90, 'math': 95, 'literature': 91}, 'Rose': {'history': 92, 'math': 96, 'literature':
# 81}, 'Kelly': {'history': 84, 'math': 85, 'literature': 87}}
# a = {key: k for key, value in a.items() for k, v in value.items() if max(value.values()) == v}
# print(a)




# Запросите у пользователя сумму, которая у него сейчас есть в бумажнике.
# Если ввести сумму, меньшую чем 0, то выбросьте исключение с текстом
# "Сумма не может быть отрицательной!"

# nums = int(input('Введите сумму в вашем кошельке: '))
# if nums < 0:
#     print("Сумма не может быть отрицательной!")
# else:
#     print('ok')




# Дан список list_ = [1, 2, 3, 4]. Выведите сумму всех этих чисел.

# list_ = [1, 2, 3, 4]
# print(sum(list_))




# Дан список с числами. Отфильтруйте этот список, оставив только четные числа.

# list_ = [1, 2, 3, 4, 5, 6]
# lst_ = []
# for i in list_:
#     if i % 2 == 0:
#         lst_.append(i)
# print(lst_)