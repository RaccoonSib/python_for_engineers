import csv
import logging
from datetime import datetime

logging.basicConfig(filename='logs.log', level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(message)s')

# Функция для вычисления разницы во времени в минутах
def time_difference(start, end):
    delta = end - start
    return delta.total_seconds() / 60

# Чтение файла и обработка данных
in_times = {}
out_times = {}

with open('activity.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Пропустить заголовок
    for row in reader:
        date_str, athlete_id, location, entry_type = row
        timestamp = datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S')

        key = (athlete_id, location)

        if entry_type == 'In':
            if key not in in_times:
                in_times[key] = timestamp
            else:
                logging.debug(f'Не зафиксировано время входа атлета {athlete_id} в {location}')

        elif entry_type == 'Out':
            if key in in_times:
                entry_time = in_times.pop(key)
                duration = time_difference(entry_time, timestamp)
                print(f"Атлет {athlete_id} провёл в {location}: {int(duration)} мин.")
            else:
                logging.debug(f'Не зафиксировано время выхода атлета {athlete_id} из {location}')

# Проверка на оставшиеся входы без выходов
for (athlete_id, location), entry_time in in_times.items():
    logging.debug(f'Не зафиксировано время выхода атлета {athlete_id} из {location}')
