def read_input():
    return open("input.txt", "r").readlines()

def resolve_tasks():
    options = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    scores = [6, 3, 0]
    
    first_results = {
        "A": ["Y", "X", "Z"],
        "B": ["Z", "Y", "X"],
        "C": ["X", "Z", "Y"]
    }
    second_results = {
        "X": 2,
        "Y": 1,
        "Z": 0
    }

    score_first = score_second = 0
    for x in read_input():
        opponent, myself = x.split()
        score_first += options[myself] + scores[first_results[opponent].index(myself)]
        score_second += scores[second_results[myself]] + options[first_results[opponent][second_results[myself]]]

    print("Task 1")
    print(score_first)

    print("Task 2")
    print(score_second)


resolve_tasks()
