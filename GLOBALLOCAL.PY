x = "global variable"

def my_function():
    y = "local variable"
    print(y)  # Prints "local variable"

my_function()
print(x)  # Prints "global variable"
# print(y)  # This would cause an error because y is a local variable and not accessible outside the function.
