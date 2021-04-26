def make_shades(alley, k):
    b = list(map(lambda x: False, range(len(alley))))
    for i in range(len(alley)):
        if alley[i] > 0:
            for j in range(int(alley[i]) * k + 1):
                if (len(b) - 1) >= (i + j):
                    b[i + j] = True
    return b

def calculate_sunny_length(shades):
    return len(list(filter(lambda x: x == False, shades)))

def main(k, array):
    if calculate_sunny_length(make_shades(array, k)) >= 10:
        print("Обгорел")
    else:
        print("Тени достаточно")