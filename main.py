# SISTEMA FORNO

#PYTHON LIBRARIES IMPORTS
import time

#CUSTOM LIBRARIES
import temperatura
import log_manager
import uart_communicator

# O resistor de potência e a ventoinha estão ambos ligados às portas GPIO e são acionados através do circuito de potência
# Resistor: GPIO 23
# Ventoinha: GPIO 24
# testar o resistor ligar por 10 segundos

#Esse modulo pode ir para outro arquivo
from gpiozero import OutputDevice
from threading import Event, Thread

resistor = OutputDevice(23)
ventoinha = OutputDevice(24)


#VARIAVEIS FORNO
ligado = False
modo_curva_temperatura = False
temperatura_externa = 9999
temperatura_referencia = 9999
temperatura_interna = 9999

#IMPORTS DOS MODULOS LOCAIS
leitor_temperatura_externa = temperatura.LeitorTemperaturaExterna()
log = log_manager.LogManager()
communicator = uart_communicator.UartCommunicator()

#FUNCOES
def estado(ligado):
	print("\n")
	print("Temperatura externa: " + str(temperatura_externa))
	print("Temperatura interna: " + str(temperatura_interna))
	
	if ligado:
		print("Forno ligado")

	else:
		print("Forno desligado")
	print("\n")

def liga():
	print("Ligando forno")
	# liga o led_1 de power


def desliga():
	print("Desligando forno")
	# desliga o led_1 de power


def watch_for_buttons():

	while True:

		request_buttons_code = b'\x01\x23\xc3'
		communicator.send_code(request_buttons_code)
		data_received = communicator.message_receiver()

		if data_received:

			button = int.from_bytes(data_received, 'little')

			if button == 1:
				print("[1] pressed")
			elif button == 2:
				print("[2] pressed")
			elif button == 3:
				print("[3] pressed")
			elif button == 4:
				print("[4] pressed")
			elif button == 5:
				print("[5] pressed")

		time.sleep(0.5)


thread_buttons_observer = Thread(target=watch_for_buttons, args=())
thread_buttons_observer.start()

#MAIN_LOOP
while True:
	print("Bem vindo ao forno")
	print("1 - Ligar forno")
	print("2 - Desligar forno")
	print("3 - Apresenta estado do forno")
	print("4 - Apresenta temperatura externa")
	op = input()

	if op == '1':
		ligado = True
		liga()

	if op == '2':
		ligado = False
		desliga()

	if op == '3':
		estado(ligado)

	if op == '4':
		external_temperature = leitor_temperatura_externa.get_external_temperature()
		print(external_temperature)
		log.create_log_entry(external_temperature)

#resistor.on()
#sleep(10)
#resistor.off()
#sleep(1)