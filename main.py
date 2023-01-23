# OVEN SYSTEM

# PYTHON LIBRARIES
import time
import struct
from threading import Thread

# CUSTOM LIBRARIES
import temperatura
import log_manager
import uart_communicator
import reflow_oven
import pid_control

# IMPORTED OBJECTS
pid = pid_control.PID()
leitor_temperatura_externa = temperatura.LeitorTemperaturaExterna()
log = log_manager.LogManager()
communicator = uart_communicator.UartCommunicator()


def turn_on():

    print("Oven set on")

    turn_on_code = b'\x01\x23\xd3'
    communicator.send_code(turn_on_code, b'\x01', 8)
    data_received = communicator.message_receiver()
    received_int = int.from_bytes(data_received, 'little')
    print(received_int)


def turn_off():

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


def watch_for_buttons(oven):

    request_buttons_code = b'\x01\x23\xc3'
    communicator.send_code(request_buttons_code)
    data_received = communicator.message_receiver()

    if data_received is not None:

        button = int.from_bytes(data_received, 'little')

        if button == 161:
            print("[1] pressed")
            oven.on = True
            turn_on()
        elif button == 162:
            print("[2] pressed")
            oven.on = False
        elif button == 163:
            print("[3] pressed")
        elif button == 164:
            print("[4] pressed")

    time.sleep(0.5)


def read_and_update_temperature_target(oven):

    request_temperature_target_code = b'\x01\x23\xc2'
    communicator.send_code(request_temperature_target_code)
    data_received = communicator.message_receiver()
    temp = struct.unpack('f', data_received)[0]
    oven.oven_temperature_target = temp
    print("Target Temperature - " + str(temp))


def read_and_update_oven_temperature(oven):

    request_oven_temperature_code = b'\x01\x23\xc1'
    communicator.send_code(request_oven_temperature_code)
    data_received = communicator.message_receiver()
    temp = struct.unpack('f', data_received)[0]
    oven.internal_temperature = temp
    print("Oven temperature - " + str(temp))


def system_update_routine():

    oven = reflow_oven.ReflowOven()

    while True:
        read_and_update_temperature_target(oven)
        watch_for_buttons(oven)
        read_and_update_oven_temperature(oven)
        watch_for_buttons(oven)
        print(pid.output(oven.oven_temperature_target, oven.internal_temperature))


system_routine_thread = Thread(target=system_update_routine, args=())
system_routine_thread.start()
