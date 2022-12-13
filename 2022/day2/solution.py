def main():
    # Who wins against who
    win = {
        'X': 'C',
        'Y': 'A',
        'Z': 'B'
    }

    score = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    translate = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    }

    totalScore = 0

    with open('input.txt') as f:
        data = f.read().splitlines()

    for line in data:
        roundScore = score[line[2]]

        if line[0] == translate[line[2]]:
            roundScore += 3
        elif win[line[2]] == line[0]:
            roundScore += 6

        totalScore += roundScore
    
    print('Total score: ' + str(totalScore))

main()