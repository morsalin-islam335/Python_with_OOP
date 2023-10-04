def outer():
    print("Starting outer function")

    def inner():
        print("Inner function start")

    print("outer function end")
    return inner


outer()()


def function(fun):
    fun()


def coding():
    print("I can code with C, C++, Java, Python")

function(coding)

