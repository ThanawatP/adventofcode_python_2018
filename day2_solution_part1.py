with open('data/day2_input.txt', 'r') as f:
    two_count = 0
    three_count = 0
    for line in f:
        line = line.strip()
        letter_dict = {}
        have_two = False
        have_three = False        
        for c in line:
            if c not in letter_dict:
                letter_dict[c] = 1
            else:
                letter_dict[c] += 1
        for count in letter_dict.values():
            if not have_two and count == 2:
                have_two = True
                two_count += 1
            elif not have_three and count == 3:
                have_three = True
                three_count += 1
            elif have_two and have_three:
                break
    print("checksum:", two_count * three_count)