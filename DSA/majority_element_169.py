from typing import List

"""Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array."""
def majorityElement(self, nums: List[int]) -> int:

    m_dict={}
    maxCount, result = 0, 0
    
    for number in nums:
        m_dict[number] =m_dict.get(number,0) + 1
        if m_dict[number] > maxCount:
            result = number
            maxCount = max(m_dict[number],maxCount)   
    
    return result