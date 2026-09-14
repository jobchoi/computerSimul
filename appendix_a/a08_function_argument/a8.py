def add():
    print("Add")

def sub():
    print("Sub")

a = [add, sub]

for i in range(len(a)):
    a[i]()


def doIt(func, x, y):
    z = func(x, y)
    return z

def add(arg1, arg2):
    return arg1 + arg2  

def sub(arg1, arg2):
    return arg1 - arg2

print("Addition:")
print(doIt(add, 2,3))   # Passing the name of the function
print("Subtraction:")
print(doIt(sub, 2,3))   # and its arguments
