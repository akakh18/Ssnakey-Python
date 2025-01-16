def get_name() -> str:
    name: str = input("Enter name: ")
    return name

if __name__ == '__main__':
    name: str = get_name()
    print(f"Hello, {name}")
