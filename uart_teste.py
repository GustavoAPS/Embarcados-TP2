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


time.sleep(0.2)
buffer = ser.read(9)
buffer_tam = len(buffer)

if buffer_tam == 9:
    data = buffer[3:7]
    crc16_recebido = buffer[7:9]
    crc16_calculado = calcula_CRC(buffer[0:7], 7).to_bytes(2, 'little')

    if crc16_recebido == crc16_calculado:
        print('Mensagem recebida: {}'.format(buffer))
        print(data)
    else:
        print('Mensagem recebida: {}'.format(buffer))
        print('CRC16 invalido')
        #return None
else:
    print('Mensagem recebida: {}'.format(buffer))
    print('Mensagem no formato incorreto, tamanho: {}'.format(buffer_tam))
    #return None
