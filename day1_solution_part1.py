with open('data/day1_input.txt', 'r') as f:
    total = 0
    for line in f:
        operation = line[0]
        number = int(line[1:])
        if operation == "-":
            number = int(line)
        total += number
    print("total:", total)