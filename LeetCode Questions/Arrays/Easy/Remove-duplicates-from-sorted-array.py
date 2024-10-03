"""Intuition
I use two pointers to efficiently identify unique elements and overwrite duplicates in-place.

Approach
I iterated through the array, comparing each element with the previous one. If it's unique, I place it in the correct position, keeping track of unique elements with a second pointer.

Complexity
Time complexity:
O(n)

Space complexity:
O(1)

Code"""
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
          return 0

        k=1
        for i in range(1,len(nums)):
          if nums[i]!=nums[i-1]:
            nums[k]=nums[i]
            k+=1
        return k
