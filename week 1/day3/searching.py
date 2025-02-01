if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7, 9, 19, 21, 128, 131, 167, 176, 189, 201, 202, 209]

    index_counter = 0

    # ვამოწმებთ არის თუ არა index_counter ინდექსზე
    while sorted_list[index_counter] != 21:
        # თუ არ არის, შემოვა აქ და გაზრდის 1-ით (გადავა შემდეგ ინდექსზე)
        index_counter = index_counter + 1

    # დავპრინტავთ რა
    print(index_counter)

    list_length = len(sorted_list)

    print(list_length)
