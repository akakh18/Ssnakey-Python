def solution(number: int) -> list:
    result: list = []

    for i in range(1, number + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 5 == 0:
            result.append("Buzz")
        elif i % 3 == 0:
            result.append("Fizz")
        else:
            result.append(str(i))
    return result


if __name__ == '__main__':
    print(solution(5) == ["1","2","Fizz","4","Buzz"])
    print(solution(15) == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])