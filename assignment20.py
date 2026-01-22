def unique_list(lst):
    return list(set(lst))

print("1. Unique elements:", unique_list([1, 2, 2, 3, 4, 4, 5, 6, 6]))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("2. Is 17 prime?", is_prime(17)) 

def print_even(lst):
    print("3. Even numbers are:")
    for i in lst:
        if i % 2 == 0:
            print(i, end=" ")
    print()

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_even(sample_list)

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print("4. Is 'Madam' palindrome?", is_palindrome("Madam"))

def min_of_three(a, b, c):
    return min(a, b, c)

print("5. Minimum of three numbers:", min_of_three(12, 5, 20))

def square_list():
    return [i**2 for i in range(1, 31)]

print("6. Squares from 1 to 30:")
print(square_list())

def inner_function():
    print("Inside inner function")

def outer_function():
    print("Inside outer function")
    inner_function()

print("7. Function inside a function:")
outer_function()

def count_upper_lower(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print("8. Upper case letters:", upper)
    print("   Lower case letters:", lower)

count_upper_lower("Hello World PYTHON")

def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    for char in alphabet:
        if char not in s:
            return False
    return True

print("9. Is pangram?",
      is_pangram("The quick brown fox jumps over the lazy dog"))

def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

print("10. Are 'listen' and 'silent' anagrams?",
      is_anagram("listen", "silent"))
