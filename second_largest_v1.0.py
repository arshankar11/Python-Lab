"""
@arshankar11 / Delhi / 13Sep26

This script finds the 2nd largest number in the list.

Complexity: 
Time: O(n)
Space: O(n)

"""

nums = [10,5,20,25,5,30,25,30]

## set() removes duplicates
unique_nums = set(nums)

if len(unique_nums) < 2:
    print("No second largest number in the list.")
else:
    unique_nums.remove(max(unique_nums))
    print(max(unique_nums))


    