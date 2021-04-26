def possible_turns(cell):
    position = []
    position2 = []
    cell2 = coordinate1(cell)
    position.append((cell2[0] + 1, cell2[1] + 2))
    position.append((cell2[0] - 1, cell2[1] + 2))
    position.append((cell2[0] + 1, cell2[1] - 2))
    position.append((cell2[0] - 1, cell2[1] - 2))
    position.append((cell2[0] + 2, cell2[1] + 1))
    position.append((cell2[0] + 2, cell2[1] - 1))
    position.append((cell2[0] - 2, cell2[1] + 1))
    position.append((cell2[0] - 2, cell2[1] - 1))
    for elem in position:
        if elem[0] > 0 and elem[1] > 0:
            position2.append(coordinate2(elem))
    position2 = sorted(position2)
    print(*position2)

def coordinate1(number1):
    number1 = ord(number1[0]) - 64, int(number1[1])
    return number1

def coordinate2(number2):
    number2 = chr(number2[0] + 64) + str(number2[1])
    return number2

possible_turns('B1')