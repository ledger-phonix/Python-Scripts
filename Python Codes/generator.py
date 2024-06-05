def my_func():
    for i in range(5000):
        yield i

gen = my_func()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))





