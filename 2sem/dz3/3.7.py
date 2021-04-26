i = input()
lst, st = [i], []
while i != '':
    i = input()
    lst.append(i)
for j in lst:
    if '#' in j:
        st = j.split()
        st.remove('#')
        if st[-1] == ' ':
            del st[-1]
        print(f'Line {lst.index(j)+1}: {" ".join(st)}')