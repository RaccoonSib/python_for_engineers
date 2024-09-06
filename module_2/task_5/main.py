from functools import reduce

elements = {
    'H': 1.008,
    'O': 15.999,
    'S': 32.066,
    'NA': 22.990,
    'CL': 35.453,
    'K': 39.098
}

# Первый способ решения. В лоб :)))

print('Первый способ решения'.upper())
def first():
    return elements['H'] * 2 + elements['S'] + elements['O'] * 4
print('H2-S-O4', first())

def second():
    return elements['H'] * 2 + elements['O']
print('H2-O', second())

def third():
    return elements['NA'] + elements['CL']
print('NA-CL', third())

def four():
    return round(elements['H'] + elements['CL'], 3)
print('H-CL', four())

def five():
    return elements['K'] + elements['CL']
print('K-CL', five())

print('\nВторой способ решения'.upper())


def calculate_molar_mass(molecule):
    # Определяем количество каждого элемента в молекуле
    counts = {
        'H': 0,
        'O': 0,
        'S': 0,
        'NA': 0,
        'CL': 0,
        'K': 0
    }

    if molecule == 'H2-S-O4':
        counts['H'] = 2
        counts['S'] = 1
        counts['O'] = 4
    elif molecule == 'H2-O':
        counts['H'] = 2
        counts['O'] = 1
    elif molecule == 'NA-CL':
        counts['NA'] = 1
        counts['CL'] = 1
    elif molecule == 'H-CL':
        counts['H'] = 1
        counts['CL'] = 1
    elif molecule == 'K-CL':
        counts['K'] = 1
        counts['CL'] = 1

    # Рассчитываем молярную массу
    molar_mass = sum(elements[element] * count for element, count in counts.items())
    return round(molar_mass, 3)

formulas = ['H2-S-O4', 'H2-O', 'NA-CL', 'H-CL', 'K-CL']

# Устанавливаем ширину для форматирования
width_molecule = max(len(molecule) for molecule in formulas) + 2
width_mass = 10

for molecule in formulas:
    print(f'{molecule:<{width_molecule}} {calculate_molar_mass(molecule):<{width_mass}}')
