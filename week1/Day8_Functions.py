# Python Lists – Examples with Top Methods

# Creating a list
fruits = ["apple", "banana", "cherry", "banana"]  # List can have duplicates

# 1️⃣ append() – Add item at the end
fruits.append("orange")  # Use when you want to add a new item
print(fruits)  # ['apple', 'banana', 'cherry', 'banana', 'orange']

# 2️⃣ insert() – Add item at specific position
fruits.insert(1, "mango")  # Use to insert at a specific index
print(fruits)  # ['apple', 'mango', 'banana', 'cherry', 'banana', 'orange']



# 3️⃣ remove() – Remove first occurrence of value
fruits.remove("banana")  # Use to delete a specific value
print(fruits)  # ['apple', 'mango', 'cherry', 'banana', 'orange']


# 4️⃣ pop() – Remove item by index (default last)
popped = fruits.pop()  # Use to remove and get last item
print(popped)  # orange
print(fruits)  # ['apple', 'mango', 'cherry', 'banana']

# 5️⃣ sort() – Sort list in ascending order
numbers = [5, 2, 9, 1]
numbers.sort()  # Use to organize data
print(numbers)  # [1, 2, 5, 9]

# 6️⃣ reverse() – Reverse list order
numbers.reverse()  # Use to reverse the list
print(numbers)  # [9, 5, 2, 1]

# 7️⃣ count() – Count occurrences of a value
print(fruits.count("banana"))  # 1 – Use to find frequency of an item

# 8️⃣ index() – Get index of first occurrence
print(fruits.index("cherry"))  # 2 – Use to locate a value

# 9️⃣ clear() – Remove all items
numbers.clear()  # Use to empty a list
print(numbers)  # []

# 🔟 copy() – Make a shallow copy
new_fruits = fruits.copy()  # Use to duplicate a list safely
print(new_fruits)  # ['apple', 'mango', 'cherry', 'banana']
