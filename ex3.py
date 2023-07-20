# ✔Создайте функцию генератор чисел Фибоначчи

def fibonacci(n):
    count = 0
    a, b = 0, 1
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print(*fibonacci(10))