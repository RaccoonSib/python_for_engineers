import math

def sin_taylor_generator(x):
    """Генератор для разложения sin(x) в ряд Тейлора."""
    term = x  # Первый член ряда
    n = 1     # Счетчик для факториала и знака
    while True:
        yield term
        term *= -x**2 / ((2*n) * (2*n + 1))  # Переход к следующему члену ряда
        n += 1

def cos_taylor_generator(x):
    """Генератор для разложения cos(x) в ряд Тейлора."""
    term = 1  # Первый член ряда
    n = 1     # Счетчик для факториала
    while True:
        yield term
        term *= -x**2 / ((2*n - 1) * (2*n))  # Переход к следующему члену ряда
        n += 1

def exp_taylor_generator(x):
    """Генератор для разложения exp(x) в ряд Тейлора."""
    term = 1  # Первый член ряда
    n = 1     # Счетчик для факториала
    while True:
        yield term
        term *= x / n  # Переход к следующему члену ряда
        n += 1

# Ввод данных
x = float(input('Введите значение угла в радианах: '))
n_terms = int(input('Введите количество элементов ряда: '))

# Вычисление суммы членов рядов
sin_sum = sum(next(sin_taylor_generator(x)) for _ in range(n_terms))
cos_sum = sum(next(cos_taylor_generator(x)) for _ in range(n_terms))
exp_sum = sum(next(exp_taylor_generator(x)) for _ in range(n_terms))

# Вычисление значений с помощью math
math_sin = math.sin(x)
math_cos = math.cos(x)
math_exp = math.exp(x)

# Вычисление разницы
sin_difference = math_sin - sin_sum
cos_difference = math_cos - cos_sum
exp_difference = math_exp - exp_sum

print(f'math.sin(x) − sin(x) = {sin_difference:.1e}')
print(f'math.cos(x) − cos(x) = {cos_difference:.1e}')
print(f'math.exp(x) − exp(x) = {exp_difference:.1e}')
