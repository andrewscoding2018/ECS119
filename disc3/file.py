import numpy as np

# Shallow copy creates a new object 
# but does not create copies of the original objects in mememory. 

# Deep copy creates a new object and recursively copies all the objects
# and references. 

# creates new variable but not new object in memory
a = [1, 2, 3, 4]
b = a # b points to same object as a

b[0] = 100
# print(a) # [1000, 2, 3, 4]

# assignment operator makes the b point to 
# same memory location as A. Modifying one
# will modify the other


b = a.copy()
b[0] = 100
# print(a) # [1, 2, 3, 4]
# print(b) # [1000, 2, 3, 4]

# why does deep copy matter
a = [1, 2, [3, 4]] # in memory, [3, 4] is a separate list and we store references to it
b = a.copy()
b[2] = 100 # this would just create a new integer index
# b[2][0] = 100 # this modifies the original list object
# print(f"B is now {b}")
# print(f"A is now {a}")


# this creates a shallow copy, the new list b contains the same elements
# but it will be a different object in memory. However, since it's a shallow 
# copy if the list contains mutable objects (like another list), changes to those 
# nested objects will still affect a and b. because the references to those objects
# are copied and not the objects themselves. 

# Deep Copy

import copy

a = [1, 2, [3, 4]]
b = copy.deepcopy(a)
b[2][0] = 100
# print("Just set b[2][0] = 100")
# print(f"The object b is equal to {b}")
# print(f"The object a is equal to {a}")


# Now for numpy arrays:

# 1) Assignment Operator (=)
# 2) Shallow Copy
# 3) Deep Copy


# 1)
a = np.array([1, 2, 3, 4])
b = a
b[1] = 99
# print(a)
# print(b) # this will be the same as A

# 2)
b = a.view()
print(a)
print(b) # this is another shallow copy. 
# numpy arrays are stored as a continuous block of memory
# which is much faster than large memory blocks
# assignment operator does not create


# Assignment operator vs. .view()
# Assignment (=): both variables reference the same underlying memory
# .view(): 
#       - new array object created
#       - but still a shallow copy
#       - shares same data buffer
#       - but diff objects, so modifying metadata = separate (shape/dtype), modifying elements will be shared


a = np.array([1, 2, 3, 4])
b = a.view()  # Creating a view of the array

print(f"Original array a: {a}")  # Output: [1 2 3 4]
print(f"View array b: {b}")  # Output: [1 2 3 4]

b[1] = 99
print(f"After modifying b[1] to 99 - array a: {a}")  # Output: [ 1 99  3  4]
print(f"After modifying b[1] to 99 - array b: {b}")  # Output: [ 1 99  3  4]

b.shape = (2, 2)
print(f"After reshaping b to (2,2) - array a: {a}")  # Output: [ 1 99  3  4]
print(f"After reshaping b to (2,2) - array b:\n{b}")  # Output: [[ 1 99] [ 3  4]]



# 3) Deep Copy
a = np.array([1, 2, 3, 4])
b = a.copy()

# Question:
"""
You are working on a weather simulation system that uses a NumPy array to store
daily temperature data for Davis across several years. To model extreme weather scenarios,
you need to make temporary changes to the data but the original data
must remain intact for future calculations.
"""

temps = np.random.uniform(low = 30, high = 115, size = (365, 10))

# create a function simulate_weather_changes(temps, extreme changes)

extreme_changes = [{"year":2, "factor":1.1}, {"year": 7, "factor": 0.9}]
# increase year 2 temps by 10%, decrease year 7 temps by 10%

def simulate_weather_changes(temps, extreme_changes):

    # each row is a day, each column is a year

    copy_data = temps.copy()

    for change in extreme_changes:
        year = change['year']
        factor = change["factor"]

        copy_data[:,year] = copy_data[:, year] * factor
    
    return copy_data

print('This should all be 1.1')
print(simulate_weather_changes(temps, extreme_changes)[:, 2] / temps[:, 2])
print("This should all be 0.9")
print(simulate_weather_changes(temps, extreme_changes)[:, 7] / temps[:, 7])
