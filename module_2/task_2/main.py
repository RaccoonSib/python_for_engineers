def get_fib_numbers(qty):
    a, b = 0, 1
    count = 0
    while True:
        if qty is not None and count >= qty:
            break
        yield a
        a, b = b, a + b
        count += 1
        if qty is not None and count >= 100:  # Ограничение на 100 элементов
            break

fib_numbers = list(get_fib_numbers(10))
assert len(fib_numbers) == 10
print(fib_numbers)

# Необходимый ответ: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]