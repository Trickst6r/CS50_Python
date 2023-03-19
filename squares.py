# Import function from other Python modules or files
from functions import square

# Import the whole function, then assign it to the square to access to the function
# import functions

# for i in range(10):
#     print(f"The square of {i} is {functions.square(i)}")


# i trong rane(10) sẽ lặp lại 10 lần từ 0 -> 9.
# Square: Bình phương mũ 2.
for i in range(10):
    print(f"The square of {i} is {square(i)}")
