def gematry(word):
    word_for_count = word.upper()
    letters_for_count = list(map(lambda x: x, word_for_count))
    values = [ord(x)-ord('A')+1 for x in letters_for_count]
    return [values, word]


def first_elem(lst):
    first, elem, index = 1000, '', None
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[j][0][0] < first:
                first = lst[j][0][0]
                elem = lst[j][1]
                index = j
    return [elem, index]


def sorting():
    word, lst, output, result = input(), [], [], None
    while word != '':
        lst.append(gematry(word))
        word = input()
    lst_for_counting = lst.copy()
    for i in range(len(lst_for_counting)):
        result = first_elem(lst)
        output.append(result[0])
        if len(lst) > 1:
            del lst[result[1]]
    print(*output, sep="\n")


sorting()