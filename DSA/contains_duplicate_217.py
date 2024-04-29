from typing import List
"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
def containsDuplicate(self, nums: List[int]) -> bool:
        dups = set()

        for num in nums:
            if num not in dups:
                dups.add(num)
            else:
                return True
        return False