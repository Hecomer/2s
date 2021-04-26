drinks = {
    'Эспрессо': [1, 0, 0],
    'Капучино': [1, 3, 0],
    'Маккиато': [2, 1, 0],
    'Кофе по-венски': [1, 0, 2],
    'Латте Маккиато': [1, 2, 1],
    'Кон Панна': [1, 0, 1]
}


def choose_coffee(preferences):
    count = 0
    for i in preferences:
        b = 0
        for j in drinks[i]:
            if ingredients[b] >= j:
                b += 1
            else:
                break
        if b == 3:
            a = 0
            for j in drinks[i]:
                ingredients[a] -= j
                a += 1
            return preferences[count]
        count += 1
    return ('К сожалению, не можем предложить Вам напиток')


ingredients = [4, 4, 0]
print(choose_coffee("Капучино, Маккиато, Эспрессо".split(", ")))
print(choose_coffee("Капучино, Маккиато, Эспрессо".split(", ")))
print(choose_coffee("Капучино, Маккиато, Эспрессо".split(", ")))