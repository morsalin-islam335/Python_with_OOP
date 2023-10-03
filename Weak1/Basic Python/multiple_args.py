def ful_name(first, second):
    name = f"{first} {second}"
    return name

print(ful_name('morsalin',"islam"))


# ** K-args

def k_args(**args):
    print(args)
    print(args['job'])

    for key, value in args.items():
        print(key, value)

k_args(first = 'Morsalin', last = 'Islam', job = "Engineer")

def multiple_return(a,b):  # we can return multiple value from a function as a tuple in normal time
    add = a + b
    sub = a - b
    mul = a * b
    dev = a / b

    # return add, sub, mul, dev  #it will return as tuple
    return [add, sub, mul, dev] # it return as list

 

print(multiple_return(20,10))
