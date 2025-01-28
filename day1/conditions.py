if __name__ == "__main__":
    n1 = input("Enter a number: ")
    n2 = input("Enter another number: ")

    n1_is_greater_then_n2: bool = n1 > n2

    if n1_is_greater_then_n2:
        print("n1 > n2")
    else:
        print("n1 isn't greater or equal to n2")
