from itertools import product

cards = ['пик', 'треф', 'бубен', 'червей']
cards.remove(input())

values_1 = [x for x in range(11)][2::]
values_2 = ['валет', 'дама', 'король', 'туз']
values = values_1 + values_2

print(*list(product(values, cards)), sep="\n")