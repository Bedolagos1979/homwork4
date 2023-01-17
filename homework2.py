n = int(input('введите натуральное число'))


def factorial(x):
    if n == 1:
        return 1
    else:
        return x * (x - 1)


print(factorial(n))
