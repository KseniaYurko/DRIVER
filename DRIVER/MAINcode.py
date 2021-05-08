import os
import datetime
import spidev

path = r'/home/pi/ADC' 
now = datetime.datetime.now()
DATE = now.strftime("%d.%m.%Y-%H:%M:%S")

spi_ch = 0
spi = spidev.SpiDev()
spi.open(0, spi_ch)
spi.max_speed_hz = 1200000
spi.cshigh = False     #cs активен в 0
spi.mode = 0b01
spi.bits_per_word = 12


def read_adc(adc_ch, vref = 10):

    msg = 0b1000110000110000  #настройка 
    reply = spi.xfer2(msg)   #cs активен между транзакциями (2)
    for i in reply:          #xfer2(list of values, [speed_hz, delay_usec, bits_per_word])  
        volt = (vref*adc)/4096
        return volt
 

try:
    os.mkdir(path)

    file = '{}.txt'.format(DATE)
    open(os.path.join(path, file), "w")

    while True:
        adc_0 = read_adc(0)
        result = adc_0*vref/4095
        file.writeln(result)
        time.sleep(0.01)


except FileExistsError:   

    file = '{}.txt'.format(DATE)
    open(os.path.join(path, file), "w")
    
        while True:
        adc_0 = read_adc(0)
        result = adc_0*vref/4095
        file.writeln(result)
        time.sleep(0.01)

finally:
    file.close()
    GPIO.cleanup()