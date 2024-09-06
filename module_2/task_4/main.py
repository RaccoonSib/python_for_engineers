import math

input_coordinates = input('Введите декартовы координаты в виде x;y: ')  # Ввод декартовых координат

x, y = map(float, input_coordinates.split(';'))

# Преобразование в полярные координаты
radius = math.sqrt(x**2 + y**2)
phi = math.atan2(y, x)

# Вывод результатов
print(f'Полярный радиус: radius={radius:.3f}')
print(f'Полярный угол: phi={phi:.3f}')
