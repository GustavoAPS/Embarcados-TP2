from csv import writer
from os.path import exists
from datetime import datetime

LOG_FILE_PATH = 'log.csv'


def create_log_file():
    with open(LOG_FILE_PATH, 'w', encoding='UTF8') as log_file:
        file_writer = writer(log_file)
        data = ["Data", "Hora", "Temperatura Ambiente"]
        file_writer.writerow(data)


class LogManager:
    def __init__(self):
        if not exists(LOG_FILE_PATH):
            create_log_file()

    def create_log_entry(self, ambient_temperature):

        now = datetime.now()
        log_date = now.strftime("%d/%m/%Y")
        log_time = now.strftime("%H:%M:%S")

        List = [log_date, log_time, ambient_temperature]

        with open(LOG_FILE_PATH, 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(List)
            f_object.close()
