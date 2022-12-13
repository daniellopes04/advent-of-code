
def main():
	elvesCount = 1
	currentCaloriesCount = 0
	elfCalories = []

	with open('input.txt') as f:
		data = f.read().splitlines()

	for line in data:
		if line == '': 
			elfCalories.append((elvesCount, currentCaloriesCount))
			elvesCount += 1
			currentCaloriesCount = 0
		else:
			currentCaloriesCount += int(line)

	sortedList = sorted(elfCalories, key=lambda elf: elf[1], reverse=True)
	topThreeCalories = sortedList[:3]
	totalCalories = sum([elf[1] for elf in topThreeCalories])

	print("Total calories by top 3 elves: "+ str(totalCalories))

main()
