def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

    initialMapping = []
    stacks = [[] for i in range(9)]

    for i in range(0, 8):
        line = data[i]
        newLine = []
        for j in range(0, len(line), 4):
            if line[j+1].isalpha():
                newLine.append(line[j+1])
            else:
                newLine.append('')
        initialMapping.append(newLine)

    for i in range(0, len(initialMapping)+1):
        for j in range(len(initialMapping)-1, -1, -1):
            if initialMapping[j][i] != '':
                stacks[i].append(initialMapping[j][i])

    for i in range(10, len(data)):
        line = data[i].split(' ')
        
        #for j in range(0, int(line[1])):
            #poppedElm = stacks[int(line[3])-1].pop()
            #stacks[int(line[5])-1].append(poppedElm)
        
        currentStack = stacks[int(line[3])-1]
        cratesToMove = currentStack[-int(line[1]):]
        
        for j in range(len(cratesToMove)):
            stacks[int(line[3])-1].pop()

        stacks[int(line[5])-1].extend(cratesToMove)

    topElements = ''
    for stack in stacks:
        if len(stack) > 0:
            topElements += stack[len(stack)-1]

    print(topElements)

main()