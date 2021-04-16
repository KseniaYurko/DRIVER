import os
import datetime
import spidev

path = r'/home/pi/ADC' 
now = datetime.datetime.now()
DATE = now.strftime("%d.%m.%Y-%H:%M:%S")

spi = spidev.SpiDev()
spi.open(0, 0)

try:
    os.mkdir(path)

    file = '{}.txt'.format(DATE)
    open(os.path.join(path, file), "w")

    #здесь должна быть программа записи значений


except FileExistsError:   

    file = '{}.txt'.format(DATE)
    open(os.path.join(path, file), "w")
    
    #здесь должна быть программа записи значений