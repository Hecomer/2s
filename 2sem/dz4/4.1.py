import sys

low_strips, high_strips, used = [], [], []
cities = {}
lst_of_countries = [i.split() for i in sys.stdin]
for j in lst_of_countries:
    city = []
    minimum = int(j[2]) // (10 ** 5) * (10 ** 5)
    maximum = (minimum + (10 ** 5))
    city.append(j[0])
    interval = f"{minimum // (10 ** 3)} - {maximum // (10 ** 3)}"
    if interval not in used:
        used.append(interval)
        cities[interval] = city
        low_strips.append(minimum // 1000)
    else:
        for k in cities[interval]:
            city.append(k)
        cities[interval] = city
low_strips.sort()
for x in range(len(low_strips)):
    print(f'{low_strips[x]} - {low_strips[x] + 100}, : ', *cities[f"{low_strips[x]} - {low_strips[x] + 100}"])
"""
Братислава Словакия 625167
Брюссель Бельгия 1154635
Будапешт Венгрия 1757618
Белград Сербия 1233796
Прага Чехия 1267449
София Болгария 1286383
Тбилиси Грузия 1118035
"""