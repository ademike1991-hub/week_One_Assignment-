# List
fruits = ["Apple", "Banana", "Orange"]

fruits.append("Mango")
fruits.remove("Banana")

print(fruits)


# Dictionary
person = {
    "name": "Michael Adekunle",
    "age": 25,
    "city": "Lagos"
}

person["age"] = 31
person["job"] = "Engineer"

print(person)


# Sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a.union(set_b))
print(set_a.intersection(set_b))