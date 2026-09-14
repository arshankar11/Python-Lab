"""
@arshankar11 / 13Sep26 / Delhi
A dictionary approach to count how many times each fruit comes in the given list.


Output:
{'apple': 2, 'banana': 2, 'guava': 1, 'mango': 1}

"""

data = ["apple","banana","guava","banana","apple","mango"]

## Intialization of counts dictionary
counts = {}

## In counts.get() , "0" is the default value when the item doesn't exist  
for item in data:
    counts[item] = counts.get(item, 0) + 1

print(counts)