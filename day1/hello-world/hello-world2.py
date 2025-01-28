def arithmetic_operation(n1: int, n2: int) -> int:
    return 2 * (n1 ** n2 + n1)


if __name__ == '__main__':
    x = 5
    y = 10
    result_1 = arithmetic_operation(x, y)
    print(result_1)

    a = 100
    b = 200
    result_2 = arithmetic_operation(a, b)

    print(result_2)
