scoring = {1:[8,2], 2:[6,9], 3:[42, 56], 20:[50, 3]}

def score(place, *numb):
    if place == 'Яблочко':
        return 50
    elif place == 'Зеленое_кольцо':
        return 25
    elif place == 'Внешнее_кольцо':
        a = scoring[numb[0]]
        return a[0]
    elif place == 'Внутреннее_кольцо':
        a = scoring[numb[0]]
        return a[1]


print(score("Яблочко"))
print(score("Внутреннее_кольцо", 3))