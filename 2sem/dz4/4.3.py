from functools import reduce
from sys import stdin
lst = list(map(str.strip, stdin))
sum_of_letters, max_sum_of_letters = 0, 0
word, word_values, count = {}, [], 0
for x in lst:
    sum_of_letters = len(x)
    word[x] = sum_of_letters if sum_of_letters > max_sum_of_letters else 'pass'
    word_values.append(word[x])

result = reduce(lambda z, y: z if z > y else y, word_values)
for i in lst:
    count += 1
    if word[i] == result:
        print(list(word)[count-1])
        break