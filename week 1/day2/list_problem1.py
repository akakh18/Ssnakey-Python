if __name__ == "__main__":
    # შემოვაყვანინოთ რიცხვი
    count: int = int(input("Enter the number of names: "))
    # დავაინიციროთ ცარიელი ლისტი
    names: list = []
    # ამ რაოდენობაჯერ შემოვაყვანინოთ სახელი
    for i in range(count):
        name: str = input("Enter a name: ")
        # თითიოეული სახელი ჩავყაროთ რაღაც ლისტში
        names.append(name)

    # დავპრინტოთ ეს ლისტი
    print(names)
