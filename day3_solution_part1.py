with open('data/day3_input.txt', 'r') as f:
    data = f.read()
    data = data.split('\n')

fabrics = []
max_i = -1
max_j = -1
for item in data:
    splited_num = item.split('@')
    fabric_id = splited_num[0].strip().strip('#')

    splited_origin_and_size = splited_num[1].split(':')
    splited_origin = splited_origin_and_size[0].split(',')
    j = int(splited_origin[0].strip())
    i = int(splited_origin[1].strip())

    splited_size = splited_origin_and_size[1].split('x')
    width = int(splited_size[0].strip())
    height = int(splited_size[1].strip())

    fabric = {
        "id": fabric_id,
        "i": i,
        "j": j,
        "width": width,
        "height": height
    }
    fabrics.append(fabric)

    if j + width > max_j:
        max_j = j + width
    if i + height > max_i:
        max_i = i + height

matrix = [['-'] * max_j for i in range(max_i)]

count = 0
for fabric in fabrics:
    for i in range(fabric['i'], fabric['i'] + fabric['height']):
        for j in range(fabric['j'], fabric['j'] + fabric['width']):
            if matrix[i][j] == '-':
                matrix[i][j] = fabric['id']
            elif matrix[i][j] != 'x':
                count += 1
                matrix[i][j] = 'x'
    print("fabric id:", fabric['id'])
print("single square inch fabric count:", count)