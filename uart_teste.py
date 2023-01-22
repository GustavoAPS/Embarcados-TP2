import time
import serial
from crc16 import calcula_CRC


ser = serial.Serial(port='/dev/serial0', baudrate=9600, timeout=1)
matricula = [4,9,9,2]

if ser.isOpen():
    print('conexao estabelecida')
else:
    print('conexao rejeitada')

comando = b'\x01\x23\xc3'
valor = b''
tamanho = 7


parte_1 = comando + bytes(matricula) + valor
parte_2 = calcula_CRC(parte_1, tamanho).to_bytes(2, 'little')
msg = parte_1 + parte_2
ser.write(msg)
