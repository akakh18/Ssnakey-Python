#            # numbers,    2,         7
def swap_indexes(lst, first_index, second_index):
    # 15
    temporary_variable = lst[first_index]

    lst[first_index] = lst[second_index]
    # [3, 1, 54, 4, 21, 23, 101, 54, 20]

    lst[second_index] = temporary_variable
    # [3, 1, 54, 4, 21, 23, 101, 15, 20]
    print(lst)


if __name__ == "__main__":
    """
        Sorting problem
    """
    #          0  1  2   3  4   5   6    7   8
    numbers = [3, 1, 15, 4, 21, 23, 101, 54, 20]


    swap_indexes(numbers, 2, 7)

    #           0  1  2   3  4   5   6    7   8
    expected = [3, 1, 54, 4, 21, 23, 101, 15, 20]

    print(numbers == expected)

# f(x) = x+2
# f(2) = 2+2 = 4
# f(4) = 4+2 = 6