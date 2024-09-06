import pandas as pd
import logging
from datetime import datetime

# Настройка логирования
logging.basicConfig(filename='logs.log', level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(message)s')

# Чтение файла
url = 'https://drive.google.com/uc?id=1dnjxkoP4PtimuD2SEAFAiztcHDyOYR7r'  # Изменённая ссылка
df = pd.read_csv(url, sep='\t')

# Инициализация словарей для хранения времени
pool_time = {}
center_time = {}

# Обработка данных
for index, row in df.iterrows():
    athlete_id = row['Athlete ID']
    entry_time = row.get('EntryTime')
    exit_time = row.get('ExitTime')
    location = row.get('Location')

    # Проверка на наличие времени входа и выхода
    if pd.isna(entry_time):
        logging.debug(f'Не зафиксировано время входа атлета {athlete_id} в {location}')
        continue  # Пропускаем эту запись

    if pd.isna(exit_time):
        logging.debug(f'Не зафиксировано время выхода атлета {athlete_id} из {location}')
        continue  # Пропускаем эту запись

    # Конвертация строкового времени в datetime
    entry_time = pd.to_datetime(entry_time)
    exit_time = pd.to_datetime(exit_time)

    # Вычисление времени проведённого в бассейне или центре
    duration = (exit_time - entry_time).total_seconds() / 60  # Время в минутах

    if location.startswith('Pool'):
        pool_time[athlete_id] = pool_time.get(athlete_id, 0) + duration
        print(f"Атлет {athlete_id} провёл в {location}: {duration:.0f} мин.")
    elif location == 'Center':
        center_time[athlete_id] = center_time.get(athlete_id, 0) + duration
        print(f"Атлет {athlete_id} провёл в {location}: {duration:.0f} мин.")

# Вывод итогов
for athlete_id, time in pool_time.items():
    print(f"Атлет {athlete_id} провёл в бассейне: {time:.0f} мин.")

for athlete_id, time in center_time.items():
    print(f"Атлет {athlete_id} провёл в центре: {time:.0f} мин.")
