import itertools

dic = input().lower().split()
prev = input().lower().split()
text = []
count = 0
for i in prev:
    for j in dic:
        b = list(''.join(i) for i in list(itertools.permutations(j, r=None)))
        if i in b[1:]:
            text.append(len(i) * '#')
            count += 1
            break
    if count == 0:
        text.append(i)
    count = 0
print(' '.join(text))