#Tuples

# A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.

# The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

# example

tuple1 = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November", "December")

print(tuple1)

# Accessing tuple elements

print(tuple1[0])


# Negative indexing

print(tuple1[-1])

# Slicing

print(tuple1[0:3])


# Changing a tuple

# Unlike lists, tuples are immutable.

# Tuples Methods

# count() - Returns the number of times a specified value occurs in a tuple

print(tuple1.count("January"))

# index() - Searches the tuple for a specified value and returns the position of where it was found

print(tuple1.index("January"))


# Loop Through a Tuple

for tuple in tuple1:
    
        print(tuple)



# Check if Item Exists

if "January" in tuple1:
        
        print("Yes, 'January' is in the months tuple")

# Tuple Length

print(len(tuple1))


# Add Items

# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.

# Create Tuple With One Item

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

tuple2 = ("January",
           
          )

print(tuple2)

# Remove Items

# Note: You cannot remove items in a tuple.



# Join Two Tuples

tuple3 = tuple1 + tuple2

print(tuple3)



