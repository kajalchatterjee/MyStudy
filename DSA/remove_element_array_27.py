from typing import List


def removeElement(nums: List[int], val: int) -> int:
  """Given an integer array nums and an integer val, remove all occurrences of 
  val in nums in-place.
  The order of the elements may be changed. Then return the number of elements in
  nums  which are not equal to val"""
  i = 0
  j = 0
  while i < len(nums):
    if nums[i] != val:
      nums[j] = nums[i]
      j += 1
    i += 1
  return j


"""    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        # Loop through all the elements of the array
        for i in range(len(nums)):
            if nums[i] != val:
                # If the element is not val
                nums[count] = nums[i]
                count += 1
        return count"""
