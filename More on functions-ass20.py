# 1. Write a python program to create a function that takes a list and returns a new list
#    with the original list's unique elements
def unique_list(lst):
    return list(set(lst))

print(unique_list([1, 2, 2, 3, 4, 4, 5]))


# 2. Write a python program to create a function that takes a number as a parameter
#    and checks if the number is prime or not
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(11))


# 3. Write a python program to create a function that prints the even numbers from a given list
def print_even_numbers(lst):
    for num in lst:
        if num % 2 == 0:
            print(num)

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_even_numbers(sample_list)


# 4. Write a python program to create a function that checks whether a passed string
#    is palindrome or not
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))


# 5. Write a python program to create a function to find the Min of three numbers
def min_of_three(a, b, c):
    return min(a, b, c)

print(min_of_three(10, 5, 20))


# 6. Write a python program to create a function and print a list where the values are
#    square of numbers between 1 and 30
def square_list():
    return [i * i for i in range(1, 31)]

print(square_list())


# 7. Write a python program to access a function inside a function
def outer_function():
    def inner_function():
        print("This is inner function")
    inner_function()

outer_function()


# 8. Write a python program to create a function that accepts a string and calculate
#    the number of upper case letters and lower case letters
def count_upper_lower(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

count_upper_lower("Hello World")


# 9. Write a python program to create a function to check whether a string is a pangram or not
def is_pangram(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set(s.lower()))

print(is_pangram("The quick brown fox jumps over the lazy dog"))


# 10. Write a python program to create a function to check whether a string is an anagram or not
def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

print(is_anagram("listen", "silent"))
