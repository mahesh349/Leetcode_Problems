"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

nums = [3,2,4]
target = 6

for i in nums:
    temp = target - i
    if temp in nums and temp+i == target:
        print([nums.index(temp),nums.index(i)])
        break
    else:
        continue

