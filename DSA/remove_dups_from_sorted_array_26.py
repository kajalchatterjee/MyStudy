from typing import List
"""Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]"""
"""Input: nums = [1,1,2]
Output: 2, nums = [1,2,_,_]"""

def removeDuplicates(nums: List[int]) -> int:
  """Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums."""

  i , j = 0 , 0
  while i < len(nums):
    if nums[i] != nums[j]:
      nums[j] = nums[i]
      j += 1
    i += 1
  return j




