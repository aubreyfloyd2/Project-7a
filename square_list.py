# Author: Aubrey Floyd
# GitHub username: aubreyfloyd2
# Date: 2/22/2023
# Description: Function that takes a list of numbers and replaces each value with the square
#              of that value.

def square_list(nums):
    """Returns the square of each value in list."""
    for num in range(len(nums)):
        nums[num] = nums[num] * nums[num]

# nums = [7, -3, 12, 9]
# square_list(nums)
# print(nums)