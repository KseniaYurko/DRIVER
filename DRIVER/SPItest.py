import spidev    #интерфейс SPI
spi = spidev.SpiDev() 
spi.open(0, 0)   #активирую порт SPI0_CE0_N (выбор из SPI0_CE0_N и SPI0_CE1_N - их всего два на плате)
                 #создаю обьект для работы с SPI и произвожу подключение
                #аргументы функции open выбирают порт

spi.lsbfirst = False
spi.cshigh = False
spi.mode = 0b01
spi.bits_per_word = 12

