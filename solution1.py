"""
Given a non-empty array of integers, every element appears twice except for one. 
Find that single one.

Note:

Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

class Solution(object):
    def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if nums == []:
        return None
    elif len(nums) == 1:
        return nums[0]

    for item in nums:
        current = nums.pop(0)
        if current not in nums:
            return current
        nums.append(current)