def prosty_dekorator(func):
    def wrapper():
        print("Przed wywołaniem")
        func()
        print("Po wywołaniu")
    return wrapper
@prosty_dekorator
def fun():
    print("Cześć")

# fun = prosty_dekorator(fun)
print("Akuku")

fun()