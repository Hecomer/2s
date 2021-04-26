import pymorphy2
import sys
morphyed = pymorphy2.MorphAnalyzer()
word = {}
word1 = {}
lst = []
biba = list(map(str.strip, sys.stdin))
text = ''
for a in biba:
    for j in a:
        if j.lower() in 'йцукенгшщзхъфывапролджэячсмитьбюё':
            text += j.lower()
        else:
            p = morphyed.parse(text)[0]
            if p.score > 0.5 and p.tag.POS == 'NOUN':
                text = morphyed.parse(text)[0].normal_form
                if text not in word.keys():
                    word[text] = 1
                else:
                    word[text] = word[text] + 1
            text = ''
for v, k in word.items():
    name = [v]
    if k in word1.keys():
        for i in word1[k]:
            name.append(i)
            name.sort()
    word1[k] = name
lst1 = [i for i in word1.keys()]
lst1.sort(reverse=True)
for i in lst1:
    for j in word1[i]:
        lst.append(j)
print(*lst[:10])