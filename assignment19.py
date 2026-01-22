def print_name():
    print("Aaqibali")

print_name() 

def print_two(a, b):
    print("First:", a)
    print("Second:", b)

print_two(10, 20)

def print_args(*args):
    print("Arguments are:")
    for i in args:
        print(i)

print_args(1, 2, 3, 4, 5)

def print_kwargs(**kwargs):
    print("Keyword arguments are:")
    for key, value in kwargs.items():
        print(key, ":", value)

print_kwargs(name="Aaqib", age=21, course="CS")

def print_list(lst):
    print("List elements are:")
    for item in lst:
        print(item)

print_list([10, 20, 30, 40])

def max_of_four(a, b, c, d):
    return max(a, b, c, d)

print("Maximum of four numbers:", max_of_four(10, 25, 5, 40))

def sum_list(lst):
    total = 0
    for i in lst:
        total += i
    return total

print("Sum of list:", sum_list([1, 2, 3, 4, 5]))

def multiply_list(lst):
    result = 1
    for i in lst:
        result *= i
    return result

print("Product of list:", multiply_list([1, 2, 3, 4, 5]))

def check_range(num, start, end):
    if start <= num <= end:
        return True
    else:
        return False

print("Number in range:", check_range(7, 1, 10))

def even_or_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

even_or_odd(15)
even_or_odd(20)

