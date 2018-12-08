with open('data/day1_input.txt', 'r') as f:
    data = f.read()
    lines = data.split('\n')
    pattern_dict = {}
    total = 0
    first_repeat = 0
    count = 0
    while first_repeat == 0:
        for line in lines:
            operation = line[0]
            number = int(line[1:])
            if operation == "-":
                number = int(line)
            total += number
            if total not in pattern_dict:
                pattern_dict[total] = 1
            else:
                first_repeat = total
                pattern_dict[total] += 1
                break
        count += 1
        print(first_repeat, count)