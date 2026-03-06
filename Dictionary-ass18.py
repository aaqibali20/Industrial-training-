# 1. Write a python program to create and print a dictionary which stores your information
my_info = {
    "name": "Aaqib Ali",
    "age": 21,
    "gender": "Male",
    "course": "B.Tech"
}
print(my_info)


# 2. Write a python program to access the items of a dictionary by referring to its key name
print(my_info["name"])
print(my_info["age"])


# 3. Write a python program to get a list of the values from a dictionary
values_list = list(my_info.values())
print(values_list)


# 4. Write a python program to change the value of a specific item by referring to its key name
my_info["age"] = 22
print(my_info)


# 5. Write a python program to print all key names in the dictionary, one by one
for key in my_info.keys():
    print(key)


# 6. Write a python program to create a dictionary that contains three dictionaries (nested)
student = {
    "student1": {"name": "Aaqib", "marks": 85},
    "student2": {"name": "Mayank", "marks": 78},
    "student3": {"name": "Dev", "marks": 90}
}
print(student)


# 7. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries
dict1 = {"a": 1}
dict2 = {"b": 2}
dict3 = {"c": 3}

combined_dict = {
    "dict1": dict1,
    "dict2": dict2,
    "dict3": dict3
}
print(combined_dict)


# 8. Write a python program to convert two lists into a dictionary
list1 = ["name", "age", "gender"]
list2 = ["Aaqib", 22, "Male"]

result_dict = dict(zip(list1, list2))
print(result_dict)


# 9. Write a python program to merge two python dictionaries into one dictionary
dict_a = {"x": 10, "y": 20}
dict_b = {"z": 30}

merged_dict = dict_a | dict_b   # Python 3.9+
print(merged_dict)


# 10. Write a python program to get the key of lowest value from the dictionary
sample_dict = {
    'C': 92,
    'Java': 66,
    'Python': 85
}

lowest_key = min(sample_dict, key=sample_dict.get)
print(lowest_key)
