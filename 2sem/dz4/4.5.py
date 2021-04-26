from sys import stdin
lst = []

for i in stdin:
    row = i.split()
    row_elems = []
    for j in row:
        row_elems.append(int(j))
    lst.append(row_elems)
res = sum(lst[0])
print('YES') if all([sum(x) == res for x in lst]) and all([sum(x) == res for x in list(zip(*lst))]) else print('NO')
