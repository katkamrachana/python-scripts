# python3.6.5
list_obj = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

print("List: ", list_obj)

print("Element at 2nd index : ", list_obj[2])
# Expected Output: 1
print("From 0th index and before 5th index: ", list_obj[0:5])
# Expected Output: [0, 1, 1, 2, 3]
print("From 3rd index and before 4th index: ", list_obj[3:4])
# Expected Output: [2]
print("Last element of the list: ", list_obj[-1])
# Expected Output: 144
print("From 5th index to after 6th element from RHS: ", list_obj[5:-6])
# Expected Output: [5, 8]

list_obj.append(233)
list_obj.append(377)
print("List after Append: ", list_obj)
# Excpected Output: 
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
list_obj.extend([610, 987])
print("List after Extend: ", list_obj)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]

# "Removes the last element. "
list_obj.pop() # 987
list_obj.pop() # 610
print("List after Pop: ", list_obj)

# "Removes the element specified with value."
list_obj.remove(377)
print("List after Remove: ", list_obj)

# Updated List: 
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

# Insert element to list. Takes args: index and value
list_obj.insert(0, 75)
print("List after Insert: ", list_obj)

list_obj.reverse()
print("List after Reverse: ", list_obj)

list_obj.sort()
print("List after Sort: ", list_obj)

print("*"*80)

pydict = {"name": "Eleven","age": 121,
	        "job_role": "gazing stars", 
        }
print("Dictionary: ", pydict)

pydict.update({"location": ["Moon", "Mars"]})
print("Updated Dictionary: ", pydict)

print("Looping Dictionary: ", pydict)
for key, value in pydict.items():
    print(key, value)

print("Changing Values in Dictionary")
if 'name' in pydict.keys():
    pydict['name'] = "Joy"
print("Updated Dictionary: ", pydict)

print("*"*80)


pytuple = ("Healthy", "minds", "are", "happy", "minds")
print("Tuple: ", pytuple)
pytuple.index("happy")
# Expected Output: 3

print("*"*80)
pyset = set()
print("Set: ", pyset)

pyset.add("go")
print("Updated Set: ", pyset)

pyset.add("coding")
print("Updated Set: ", pyset)

pyset.add("go") # no effect
print("Updated Set: ", pyset)