def main():
    # Who wins against who 
    win = {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    } 

    lose = {
        'A': 'B',
        'B': 'C',
        'C': 'A'
    }

    score = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    totalScore = 0

    with open('input.txt') as f:
        data = f.read().splitlines()

    for line in data:
        roundScore = 0

        if line[2] == 'X':
            roundScore = score[win[line[0]]]
        elif line[2] == 'Y':
            roundScore = score[line[0]]
            roundScore += 3
        else:
            roundScore = score[lose[line[0]]]
            roundScore += 6

        totalScore += roundScore
    
    print('Total score: ' + str(totalScore))

main()