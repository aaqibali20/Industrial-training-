info = {
    "name": "Aaqib Ali",
    "age": 20,
    "gender": "Male",
    "course": "Computer Science"
}
print("1. My Information Dictionary:")
print(info)
print("\n2. Accessing items using keys:")
print("Name:", info["name"])
print("Age:", info["age"])
values_list = list(info.values())
print("\n3. List of values:")
print(values_list)

info["age"] = 21
print("\n4. After changing age:")
print(info)

print("\n5. All key names:")
for key in info.keys():
    print(key)

nested_dict = {
    "student1": {"name": "Aaqib", "marks": 85},
    "student2": {"name": "Dev", "marks": 90},
    "student3": {"name": "Zeeshan", "marks": 88}
}
print("\n6. Nested Dictionary:")
print(nested_dict)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}

main_dict = {
    "dict1": dict1,
    "dict2": dict2,
    "dict3": dict3
}
print("\n7. Dictionary containing three dictionaries:")
print(main_dict) 

list1 = ["name", "age", "gender"]
list2 = ["Aaqib", 21, "Male"]

converted_dict = dict(zip(list1, list2))
print("\n8. Dictionary from two lists:")
print(converted_dict)

d1 = {"x": 10, "y": 20}
d2 = {"z": 30, "w": 40}

merged_dict = {**d1, **d2}
print("\n9. Merged Dictionary:")
print(merged_dict)

sample_dict = {
    'C': 92,
    'Java': 66,
    'Python': 85
}

lowest_key = min(sample_dict, key=sample_dict.get)
print("\n10. Key with lowest value:")
print(lowest_key)