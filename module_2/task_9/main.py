import crc8

def encode_message(message):
    encoded_parts = []

    for char in message:
        # Вычисляем CRC8 для символа
        crc_value = crc8.crc8()
        crc_value.update(char.encode())
        crc_checksum = crc_value.hexdigest()

        # Конвертируем символ и его контрольную сумму в бинарный вид
        binary_char = format(ord(char), '08b')
        binary_crc = format(int(crc_checksum, 16), '08b')
        encoded_parts.append(binary_char + ' ' + binary_crc)

    return ' '.join(encoded_parts)

def decode_message(encoded_message):
    decoded_chars = []
    errors = []

    parts = encoded_message.split()  # Разбиваем по пробелам

    for i in range(0, len(parts), 2):
        binary_char = parts[i]
        binary_crc = parts[i + 1]

        char = chr(int(binary_char, 2))  # Декодируем символ

        # Проверяем контрольную сумму
        expected_crc = crc8.crc8()
        expected_crc.update(char.encode())
        expected_checksum = expected_crc.hexdigest()

        if binary_crc != format(int(expected_checksum, 16), '08b'):
            errors.append((i // 2, char, binary_crc, expected_checksum))

        decoded_chars.append(char)

    return ''.join(decoded_chars), errors

def main():
    message_type = int(input('Введите тип (1 — кодер и декодер, 2 — декодер): '))

    if message_type == 1:
        message = input('Введите сообщение: ')
        encoded_message = encode_message(message)
        print('Кодированное сообщение:', encoded_message)

        decoded_message, _ = decode_message(encoded_message)
        print('Декодированное сообщение:', decoded_message)

    elif message_type == 2:
        encoded_message = input('Введите кодированное сообщение: ')
        decoded_message, errors = decode_message(encoded_message)

        if not errors:
            print('Все контрольные суммы верны.')
        else:
            for index, char, received_crc, expected_crc in errors:
                print(f'Ошибка в символе {char} с индексом {index}.')
                print(f'Символ: {char}')
                print(f'crc8: {expected_crc}')
                print(f'crc8 (полученное): {received_crc}')

        print('Декодированное сообщение:', decoded_message)

if __name__ == '__main__':
    main()
