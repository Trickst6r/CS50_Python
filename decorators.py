# Decorator is going to be a function that takes a function of input
# and returns a modified version of that input as output


# Create a function that modifies another function
# by announcing that the function is about to run and that the
# function has completed run.
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")

    return wrapper


# Add announce() decorator to this function
@announce
def hello():
    print("Hello, world!")


# Call the function
hello()

# Step by step:
# 1. Taking the function f
# 2. Creating a new function that just announces,
# via print statement before and after the function is done running
