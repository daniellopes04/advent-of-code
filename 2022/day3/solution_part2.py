def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

    sumPriorities = 0

    for i in range(0, len(data), 3):
        first = data[i]
        second = data[i + 1]
        third = data[i + 2]

        commonChar = list(set(first).intersection(second).intersection(third))[0]

        # ASCII entry for 'a' is 97
        if (commonChar.islower()):
            sumPriorities += ord(commonChar) - 96

        # ASCII entry for 'A' is 65
        else:
            sumPriorities += ord(commonChar) - 64 + 26

    print('Sum of priorities: ' + str(sumPriorities))
    
main()