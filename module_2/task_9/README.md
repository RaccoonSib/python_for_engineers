Реализуйте вычисление контрольной суммы для каждой буквы сообщения:

На вход передаётся некоторое сообщение.
Вы разбиваете его на символы, вычисляете crc8 для каждого символа, выводите символ и его контрольную
сумму в виде 0 и 1, то есть в бинарной форме.
Создаёте декодер для получения сообщения, проверки контрольной суммы для каждого символа.
В случае обнаружения проблем с контрольной суммой выводите на консоль и в файл ошибку. Также передаёте тело
сообщения и контрольную сумму.