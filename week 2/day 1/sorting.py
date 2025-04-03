# Finds minimum element in list starting from start_index
def find_minimum_index_from(start_index: int, lst: list) -> int:
    result: int = start_index

    for i in range(start_index, len(lst)):
        if lst[i] < lst[result]:
            result = i

    return result


# Swaps elements in list
def swap(first_index: int, second_index: int, lst: list) -> None:
    # 14
    temp: int = lst[first_index]
    # [2, 7, 3, 9, 13, 13, 5, 8, 4]
    lst[first_index] = lst[second_index]
    # [2, 7, 3, 9, 13, 14, 5, 8, 4]
    lst[second_index] = temp


def my_sort(lst: list) -> list:
    # Insertion sort
    for i in range(len(lst)):
        current_minimum_index = find_minimum_index_from(i, lst)
        swap(i, current_minimum_index, lst)

    return lst


if __name__ == "__main__":
    numbers: list = [2, 7, 3, 9, 14, 13, 5, 8, 4]
    print(my_sort(numbers))
    print(my_sort(numbers) == sorted(numbers))