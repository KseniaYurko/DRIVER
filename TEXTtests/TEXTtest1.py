import os

path = r'C:/Users/user/Desktop/DRIVER' 
    
i = 0

with open(os.path.join(path,'test.txt'), 'r') as counter_file:     

        i = int(counter_file.read())
        counter_file.seek(0)
        counter_file.close()        

        i += 1      

with open(os.path.join(path,'test.txt'), 'w+') as counter_file:     

        counter_file.write(str(i))
        counter_file.seek(0)
        counter_file.close() 