# f = open('text.txt', 'r')
# # print(f)
# for line in f:
#     print(type(line))



# режимы работы с файлами:
# 1. read(r) - чтение из файла
# 2. write(w) - запись в файл (файл перезаписывается)
# 3. append(a) - записывает данные в конец файлам
# 4. exclusive(x) - открывает файл для записи, только если такого файла пока не существует
# 'rt' - read text
# 'wt' - write text
# 'w+' - для записи и для чтения

# try:
#     f = open('text.txt', 'wt')
#     f.write('Как дела как дела это новый кадиллак')
# finally:
#     f.close()

# f = open('text.txt', 'r')
# file_content = f.read()
# print(file_content)
# print(f.read(36))
# print('=============================')
# print(f.read())
# f.seek(0)
# print(f.tell())
# f.seek(50)
# print(f.read())
# print(f.)
# content = f.readlines()
# content_2 = []
# for item in content:
#     content_2.append(item.replace('\n', ''))
# print(content_2)

# f = open('text.txt', 'w+')
# f.write('string\n')
# f.writelines(['string2\n', 'string3\n'])
# f.close

# f = open('text.txt', 'a+')
# f.writelines(['hello world', 'world hello'])
# f.close


def manage():
    f = open('text.txt', 'a+')
    a = input('Введите вашу строку: ')
    f.write(a + '\n')
    print('Строчка успешно записана')
    f.close()
    g = input('Хотите повторить? да/нет: ')
    if g == 'да':
        manage()
    elif g == 'нет':
        print('Ок')
manage()