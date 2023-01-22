# SISTEMA FORNO	

# O resistor de potência e a ventoinha estão ambos ligados às portas GPIO e são acionados através do circuito de potência
# Resistor: GPIO 23
# Ventoinha: GPIO 24
# testar o resistor ligar por 10 segundos

from gpiozero import OutputDevice


resistor = OutputDevice(23)
ventoinha = OutputDevice(24)


#VARIAVEIS
ligado = False
modo_curva_temperatura = False
temperatura_externa = 22.0
temperatura_referencia = 40.0
temperatura_interna = 20.0

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
while 1 == 4:
	print("Bem vindo ao forno")
	print("1 - Ligar forno")
	print("2 - Desligar forno")
	print("3 - Apresenta estado do forno")
	op = input()

	if op == '1':
		ligado = True
		liga()

	if op == '2':
		ligado = False
		desliga()

	if op == '3':
		estado(ligado)


resistor.on()
sleep(10)
resistor.off()
sleep(1)