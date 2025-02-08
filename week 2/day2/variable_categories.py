from subprocess import list2cmdline


def solution(arg: any) -> any:
    arg.append(5)


if __name__ == '__main__':
    l: list = list()
    l2: list = list()
    l.append(1)
    l.append(2)
    l.append(3)

    print(l)
    print(l2)
