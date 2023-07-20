# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def parse_path(path):
    filepath, extension = os.path.splitext(path)
    dirname, filename = os.path.split(filepath)
    return (dirname, filename, extension)

path = 'C:/Users/Diana/Desktop/python_2/homework5/ex1.py'
data = parse_path(path)
print(*data)

