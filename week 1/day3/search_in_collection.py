if __name__ == '__main__':
    collection: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    n: int = 0

    while n != 105001:
        n: int = int(input("Enter the number: "))
        if n in collection:
            print('Yes')
        else:
            print('No')