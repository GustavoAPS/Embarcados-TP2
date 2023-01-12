# SISTEMA FORNO	

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
while True:
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
