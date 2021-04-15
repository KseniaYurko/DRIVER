import os

path = r'C:/Users/user/Desktop/Hello_world.txt' 

file = open(path, 'w')  # создаем txt файл
file.write('Hello, World!') # записываем текст
file.close()  # закрываем файл