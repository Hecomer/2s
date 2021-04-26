def fractal_print(obj):
    fractal2 = obj.copy()
    ind = fractal2.index(obj)
    del fractal2[ind]
    fractal2.insert(ind, obj)
    print(fractal2)


fractal = [3]
fractal.append(fractal)
fractal.append(2)
fractal_print(fractal)