import os

path = r'C:/Users/user/Desktop/DRIVER' 

                 #счетчик запусков программы
file = 'NUM.txt'
i = 0 

try:
    os.mkdir(path)
    with open(os.path.join(path,'NUM.txt'), 'w') as counter_file:
        counter_file.write(str(i))
        counter_file.close()

    file = 'Data{}.txt'.format(i)
    open(os.path.join(path, file), "w")

    #здесь должна быть программа записи значений

    i+=1

except FileExistsError:

    with open(os.path.join(path,'NUM.txt'), 'r') as counter_file:     
        i = int(counter_file.read())
        counter_file.seek(0)
        counter_file.close()        

        i += 1      

    with open(os.path.join(path,'NUM.txt'), 'w+') as counter_file:     
        counter_file.write(str(i))
        counter_file.seek(0)
        counter_file.close()              # увеличиваем счетчик на 1

    file = 'Data{}.txt'.format(i)
    open(os.path.join(path, file), "w")
    
    #здесь должна быть программа записи значений