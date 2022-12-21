def main():
    with open('input.txt') as f:
        data = f.read().splitlines()

    line = data[0]
    lenMessage = 14
    marker = ''
    processedChars = 0
    
    for i in range(0, len(line)-lenMessage-1):
        currentMarker = [line[x] for x in range(i, i+lenMessage)]

        if len(currentMarker) == len(set(currentMarker)):
            marker = ''.join(x for x in currentMarker)
            processedChars = i+lenMessage
            break
    
    print(marker)
    print(processedChars)

main()