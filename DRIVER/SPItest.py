reply = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
adc = 0
#1111100000   [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
vref = 3.3
for n in reply:
    adc1 = (adc << 8) + n
    binary1 = bin(adc1)[2:].zfill(8) 
    print(adc1, '  ', binary1)
    adc2 = adc >> 1
    binary2 = bin(adc2)[2:].zfill(8)
    print(adc2, '  ', binary2)
adc = adc2
voltage = (vref * adc) / 1024
print (voltage)

