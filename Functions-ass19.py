# 1. Write a python program to create a simple function which prints “TasiNCoder”
def print_name():
    print("Aaqib Ali")

print_name()


# 2. Write a python program to create a function which expects two arguments and print them
def print_two_args(a, b):
    print(a, b)

print_two_args("Hello", "World")


# 3. Write a python program to create a function which expects an unknown number of arguments
def print_args(*args):
    for item in args:
        print(item)

print_args(1, 2, 3, 4, 5)


# 4. Write a python program to create a function which expects kwargs arguments
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_kwargs(name="Aaqib", age=22, course="B.Tech")


# 5. Write a python program to create a function which expects a list as an argument
def print_list(my_list):
    for item in my_list:
        print(item)

print_list([10, 20, 30, 40])


# 6. Write a python program to create a function that finds a maximum of four numbers
def max_of_four(a, b, c, d):
    return max(a, b, c, d)

print(max_of_four(10, 45, 23, 67))


# 7. Write a python program to sum all the numbers in a list
def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4, 5]))


# 8. Write a python program to multiply all the numbers in a list
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print(multiply_list([1, 2, 3, 4]))


# 9. Write a python program to create a function to check whether a number falls in a given range
def check_range(num, start, end):
    if start <= num <= end:
        return True
    else:
        return False

print(check_range(5, 1, 10))


# 10. Write a python program to create a function to check whether a given number is even or odd
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(7))


