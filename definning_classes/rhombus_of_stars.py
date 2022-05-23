def size_of_rhombus():
    return int(input())


def print_solution(number: int) -> print:
    for num in range(number):
        print((" " * (number - 1 - num) + "* " * (num + 1)).rstrip())

    for num in range(1, number):
        print((" " * num + "* " * (number - num)).rstrip())


number_of_rhombus = size_of_rhombus()
print_solution(number_of_rhombus)
