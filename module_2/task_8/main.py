import csv
from datetime import datetime
from typing import List, Dict

def read_csv(filename: str) -> List[Dict[str, str]]:
    data = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file, delimiter=',')
        for row in reader:
            data.append(row)
    return data

def log_error(message: str):
    with open('logs.log', 'a') as log_file:
        log_file.write(f"{datetime.now()} | ERROR | {message}\n")

def calculate_time(records: List[Dict[str, str]]):
    pool_times = {}
    complex_times = {}

    for record in records:
        athlete_id = record.get('athlete_id')
        entry_time = record.get('entry_time')
        exit_time = record.get('exit_time')
        location = record.get('location')

        if not entry_time:
            log_error(f'Не зафиксировано время входа атлета {athlete_id} в {location}')
            continue

        if not exit_time:
            log_error(f'Не зафиксировано время выхода атлета {athlete_id} из {location}')
            continue

        try:
            entry_dt = datetime.strptime(entry_time, '%Y-%m-%d %H:%M:%S')
            exit_dt = datetime.strptime(exit_time, '%Y-%m-%d %H:%M:%S')

            time_in_pool = (exit_dt - entry_dt).total_seconds() / 60  # в минутах
            if location.startswith('Pool'):
                pool_times[athlete_id] = pool_times.get(athlete_id, 0) + time_in_pool
            else:
                complex_times[athlete_id] = complex_times.get(athlete_id, 0) + time_in_pool

        except ValueError as e:
            log_error(f'Ошибка в данных времени для атлета {athlete_id}: {e}')

    return pool_times, complex_times

def main():
    filename = 'C:/Users/vladi/OneDrive/Desktop/module_2/task_8/activity.csv'  # Укажите путь к вашему файлу
    records = read_csv(filename)
    pool_times, complex_times = calculate_time(records)

    for athlete_id, minutes in pool_times.items():
        print(f'Атлет {athlete_id} провёл в бассейне: {int(minutes)} мин.')

    for athlete_id, minutes in complex_times.items():
        print(f'Атлет {athlete_id} провёл в комплексе: {int(minutes)} мин.')

if __name__ == '__main__':
    main()
