def announce(f):
    def wrapper():
        print("About to run function")
        f()
        print("Function execution completed")
    return wrapper


@announce
def hello():
    print("Hello, world")


hello()
