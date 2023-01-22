# SISTEMA FORNO
import temperatura
import log_manager

# O resistor de potência e a ventoinha estão ambos ligados às portas GPIO e são acionados através do circuito de potência
# Resistor: GPIO 23
# Ventoinha: GPIO 24
# testar o resistor ligar por 10 segundos


#Esse modulo pode ir para outro arquivo
from gpiozero import OutputDevice
resistor = OutputDevice(23)
ventoinha = OutputDevice(24)


#VARIAVEIS FORNO
ligado = False
modo_curva_temperatura = False
temperatura_externa = 9999
temperatura_referencia = 9999
temperatura_interna = 9999

leitor_temperatura_externa = temperatura.LeitorTemperaturaExterna()
log = log_manager.LogManager()

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