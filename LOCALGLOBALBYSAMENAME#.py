x = "global"

def my_function():
    x = "local"
    print("Inside function:", x)  # Prints "local"

my_function()
print("Outside function:", x)  # Prints "global"
