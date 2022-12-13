def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

    sumPriorities = 0

    for line in data:
        listLength = len(line)
        firstHalf = line[:listLength // 2]
        secondHalf = line[listLength // 2:]

        commonChar = list(set(firstHalf).intersection(secondHalf))[0]

        # ASCII entry for 'a' is 97
        if (commonChar.islower()):
            sumPriorities += ord(commonChar) - 96

        # ASCII entry for 'A' is 65
        else:
            sumPriorities += ord(commonChar) - 64 + 26

    print('Sum of priorities: ' + str(sumPriorities))
    
main()