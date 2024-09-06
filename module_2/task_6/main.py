import logging
import re

# Настройка логирования
logging.basicConfig(filename='logs_task_6.log', level=logging.ERROR,
                    format='%(asctime)s | %(levelname)s | %(message)s')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero")
    return x / y

def parse_expression(expression):
    # Убираем лишние пробелы и заменяем запятую на точку
    expression = expression.replace(',', '.').strip()
    # Регулярное выражение для поиска чисел и операторов
    pattern = r'([-+]?\d*\.?\d+|\d+|\+|\-|\*|\/)'
    tokens = re.findall(pattern, expression)

    if len(tokens) < 3:
        raise ValueError("Invalid expression")

    # Преобразуем числа в float
    try:
        num1 = float(tokens[0])
        operator = tokens[1]
        num2 = float(tokens[2])
    except ValueError as e:
        raise ValueError(f"could not convert string to float: '{tokens[0]}'") from e

    return num1, operator, num2

def calculate(expression):
    try:
        num1, operator, num2 = parse_expression(expression)

        if operator == '+':
            return add(num1, num2)
        elif operator == '-':
            return subtract(num1, num2)
        elif operator == '*':
            return multiply(num1, num2)
        elif operator == '/':
            return divide(num1, num2)
        else:
            raise ValueError(f"Unknown operator: '{operator}'")

    except Exception as e:
        logging.error(f"Line #{line_number}: {str(e)}")
        return None


if __name__ == "__main__":
    results = []

    with open('exprs_task_6.txt', 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if line.strip():  # Игнорируем пустые строки
                result = calculate(line)
                if result is not None:
                    results.append(f"{line_number} {result}")

    # Запись результатов в файл
    with open('results_task_6.txt', 'w') as result_file:
        for res in results:
            result_file.write(res + '\n')

