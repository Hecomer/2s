def cached(fn):
    def cach():
        with open("cached_files.txt", "w", encoding='utf-8') as file:
            file.write(fn)
        file.close()
    return cach


@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib(10)