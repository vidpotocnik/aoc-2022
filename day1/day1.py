from urllib.request import urlopen


def read_input():
    with open('input.txt') as f:
        lines = [x for x in f.read().split("\n\n")]
    return lines

def resolve_task():
    data = read_input()
    elf = [line.split() for line in data]
    calories = sorted([sum(int(snack) for snack in snacks) for snacks in elf], reverse=True)

    print ('Task 1')
    print(calories[0])

    print('Task 2')
    print(sum(calories[:3]))

resolve_task()

