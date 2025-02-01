if __name__ == '__main__':
    and_result1: bool = True and False  # False
    and_result2: bool = True and True   # True
    and_result3: bool = False and True  # False
    and_result4: bool = False and False # False

    print("And")
    print("True and False:", and_result1)
    print("True and True:", and_result2)
    print("False and True:", and_result3)
    print("False and False:", and_result4)

    print("__________________________")

    or_result1: bool = True or False  # True
    or_result2: bool = True or True   # True
    or_result3: bool = False or True  # True
    or_result4: bool = False or False # False

    print("Or")
    print("True or False:", or_result1)
    print("True or True:", or_result2)
    print("False or True:", or_result3)
    print("False or False:", or_result4)
