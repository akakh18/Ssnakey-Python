def sum_of_numbers(n, m):
    #16           #14 #2
    result_sum = n + m
    #16
    return result_sum


if __name__ == "__main__":
    first_number = int(input("First number: "))
    second_number = int(input("Second number: "))
    result = sum_of_numbers(first_number, second_number)
    print(result)
