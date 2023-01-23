from time import sleep
from gpiozero import OutputDevice


resistor = OutputDevice(23)
ventoinha = OutputDevice(24)

resistor.off()
sleep(5)
