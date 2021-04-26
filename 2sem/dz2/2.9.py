def solve(*coefficients):
    if len(coefficients) == 1:
        if coefficients[0] == 0:
            return ['Любое значение']
        else:
            return [None]
    elif len(coefficients) == 2:
        return [-(coefficients[1] / coefficients[0])]
    elif len(coefficients) == 3:
        D = coefficients[1] ** 2 - 4 * coefficients[0] * coefficients[2]
        if D == 0:
            return [(-coefficients[1]) / (2 * coefficients[0])]
        elif D < 0:
            return [None]
        elif D > 0:
            return [(-coefficients[1] + D ** (1/2)) / (2 * coefficients[0]), (-coefficients[1] - D ** (1/2)) / (2 * coefficients[0])]
    else:
        return [None]


print(sorted(solve(1, 2, 4)))