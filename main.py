# SISTEMA FORNO

# PYTHON LIBRARIES IMPORTS
import time
import struct

# CUSTOM LIBRARIES
import temperatura
import log_manager
import uart_communicator

# O resistor de potência e a ventoinha estão ambos ligados às portas GPIO e são acionados através do circuito de potência
# Resistor: GPIO 23
# Ventoinha: GPIO 24
# testar o resistor ligar por 10 segundos

# Esse modulo pode ir para outro arquivo
from gpiozero import OutputDevice
from threading import Event, Thread

resistor = OutputDevice(23)
ventoinha = OutputDevice(24)

# ----------------------------------------------------- #
# OVEN VARIABLES
# it can be on hearing commands and working
# to work it needs to be on
oven_is_on = False
working = False
temperature_curve_mode = False
outside_temperature = 9999
oven_temperature_target = 9999
internal_temperature = 9999

# IMPORTED OBJECTS
leitor_temperatura_externa = temperatura.LeitorTemperaturaExterna()
log = log_manager.LogManager()
communicator = uart_communicator.UartCommunicator()


def turn_on(oven_is_on_state):
    oven_is_on_state = True
    print("Oven set on")

    turn_on_code = b'\x01\x23\xd3'
    communicator.send_code(turn_on_code, b'\x01', 8)
    data_received = communicator.message_receiver()
    received_int = int.from_bytes(data_received, 'little')
    print(received_int)


def turn_off(oven_is_on_state):
    oven_is_on_state = False
    print("Oven set off")

    turn_off_code = b'\x01\x23\xd3'
    communicator.send_code(turn_off_code, b'\x00', 8)
    data_received = communicator.message_receiver()
    received_int = int.from_bytes(data_received, 'little')
    print(received_int)


def start_work():
    pass


def stop_work():
    pass


def watch_for_buttons():

    request_buttons_code = b'\x01\x23\xc3'
    communicator.send_code(request_buttons_code)
    data_received = communicator.message_receiver()

    if data_received is not None:

        button = int.from_bytes(data_received, 'little')

        if button == 161:
            print("[1] pressed")
            turn_on(oven_is_on)
        elif button == 162:
            print("[2] pressed")
            turn_off(oven_is_on)
        elif button == 163:
            print("[3] pressed")
        elif button == 164:
            print("[4] pressed")

    time.sleep(0.5)


def read_and_update_temperature_target():

    request_temperature_target_code = b'\x01\x23\xc2'
    communicator.send_code(request_temperature_target_code)
    data_received = communicator.message_receiver()
    temp = struct.unpack('f', data_received)[0]
    print("Target Temperature - " + str(temp))


def read_and_update_oven_temperature():

    request_oven_temperature_code = b'\x01\x23\xc1'
    communicator.send_code(request_oven_temperature_code)
    data_received = communicator.message_receiver()
    temp = struct.unpack('f', data_received)[0]
    print("Oven temperature - " + str(temp))



def system_update_routine():
    while True:
        read_and_update_temperature_target()
        watch_for_buttons()
        read_and_update_oven_temperature()
        watch_for_buttons()


thread_buttons_observer = Thread(target=system_update_routine, args=())
thread_buttons_observer.start()

# MAIN_LOOP
while True:
    print("Bem vindo ao forno")
    print("1 - Ligar forno")
    print("2 - Desligar forno")
    print("3 - Apresenta estado do forno")
    print("4 - Apresenta temperatura externa")
    op = input()

    if op == '1':
        pass


    if op == '2':
        pass


    if op == '3':
        pass

    if op == '4':
        outside_temperature = leitor_temperatura_externa.get_external_temperature()
        print(outside_temperature)
        log.create_log_entry(outside_temperature)

# resistor.on()
# sleep(10)
# resistor.off()
# sleep(1)
