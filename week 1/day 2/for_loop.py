if __name__ == "__main__":
    sum: int = 0

    for i in range(5):
        number: int = int(input("Enter a number: "))
        sum = sum + number

        print("Now the sum is: ", sum)

    print(sum)
