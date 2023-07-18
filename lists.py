# List

# example List of Months

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November", "December"]

print(months[-3])

#list methods

# append() - Adds an element at the end of the list

months.append("New Month")

print(months)

# clear() - Removes all the elements from the list

months.clear()

print(months)

# copy() - Returns a copy of the list

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November", "December"]

new_months = months.copy()

print(new_months)

# count() - Returns the number of elements with the specified value

print(months.count("January"))

# extend() - Add the elements of a list (or any iterable), to the end of the current list

new_months.extend(months)

print(new_months)

# index() - Returns the index of the first element with the specified value

print(months.index("January"))

# insert() - Adds an element at the specified position

months.insert(0, "New Month")

print(months)

# pop() - Removes the element at the specified position

months.pop(0)

print(months)

# remove() - Removes the first item with the specified value

months.remove("January")

print(months)

# reverse() - Reverses the order of the list

months.reverse()

print(months)

# sort() - Sorts the list

months.sort()

print(months)




   