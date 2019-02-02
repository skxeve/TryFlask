def deco(func):
    def wrapper(*args, **kwargs):
        print("--- start ---")
        func(*args, **kwargs)
        print("--- end ---")
    return wrapper

@deco
def test():
    print("hello world!")

test()



def deco2(func):
    def wrapper(*args, **kwargs):
        print("***** {} *****".format(func(*args, **kwargs)))
    return wrapper


@deco2
def test2():
    return "Decorate return value!"

ret = test2()
print("Ret is {}".format(ret))
