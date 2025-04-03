def find_min_number_index(lst, idx):
    if lst == []:
        return -1

    result = idx
    current_minimum = lst[idx]

    for i_ in range(idx, len(lst)):
        if lst[i_] < current_minimum:
            current_minimum = lst[i_]
            result = i_

    return result

def swap_indexes(lst, first_index, second_index):
    temporary_variable = lst[first_index]
    lst[first_index] = lst[second_index]
    lst[second_index] = temporary_variable


def my_sort(unsorted_list):
    result = unsorted_list
    for i in range(0, len(unsorted_list)):
        # find min number's index
        min_num_index = find_min_number_index(result, i)
        # swap current to minimum
        swap_indexes(result, i, min_num_index)
    return result

if __name__ == "__main__":
    numbers = [5, 2, 6, 13, 4, 7, 9, 8]

    sorted_numbers = my_sort(numbers)
    print(sorted_numbers)

#  +
# [5, 2, 6, 13, 4, 7, 9, 8]
#     +
# [2, 5, 6, 13, 4, 7, 9, 8]
#        #
# [2, 4, 6, 13, 5, 7, 9, 8]
#           #
# [2, 4, 5, 13, 6, 7, 9, 8]
#              #
# [2, 4, 5, 6, 13, 7, 9, 8]
#                 #
# [2, 4, 5, 6, 7, 13, 9, 8]
                     #
# [2, 4, 5, 6, 7, 8, 9, 13]
#                       #
# [2, 4, 5, 6, 7, 8, 9, 13]
