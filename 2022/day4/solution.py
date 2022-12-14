def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

    sum = 0

    for line in data:
        sections = line.split(',')
        rangeOne = sections[0].split('-')
        rangeTwo = sections[1].split('-')

        firstSet = set(range(int(rangeOne[0]), int(rangeOne[1]) + 1))
        secondSet = set(range(int(rangeTwo[0]), int(rangeTwo[1]) + 1))

        # if (firstSet.issubset(secondSet) or secondSet.issubset(firstSet)):
        if (firstSet.intersection(secondSet) or secondSet.intersection(firstSet)):
            sum += 1        

    print('Number of inefficient pairs: ' + str(sum))
    
main()