def test(*args, **kwargs):
    print(args, kwargs)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


test(1, 2, 6, 7, 'string', True, name='Petya', address='Barnaul')
number = int(input("Введите число для вычисления факториала: "))
print("Факториал числа", number, "равен", factorial(number))
