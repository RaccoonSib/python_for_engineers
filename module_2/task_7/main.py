def caesar_cipher(message, shift):
    result = ''

    for char in message:
        if char.isalpha():  # Проверяем, является ли символ буквой
            shift_base = ord('А') if char.isupper() else ord('а')
            # Применяем шифр Цезаря
            result += chr((ord(char) - shift_base + shift) % 32 + shift_base)
        else:
            result += char  # Неизменяемые символы (пробелы, знаки препинания)

    return result

def main():
    shift = int(input('Введите смещение: '))
    message = input('Введите сообщение: ')

    # Шифрование и расшифровка
    encrypted_message = caesar_cipher(message, shift)
    decrypted_message = caesar_cipher(encrypted_message, -shift)

    print('Шифрованное сообщение:', encrypted_message)
    print('Расшифрованное сообщение:', decrypted_message)

if __name__ == '__main__':
    main()
