from time import sleep
from gpiozero import OutputDevice


resistor = OutputDevice(23)
ventoinha = OutputDevice(24)


resistor.on()
sleep(10)
resistor.off()
sleep(1)
