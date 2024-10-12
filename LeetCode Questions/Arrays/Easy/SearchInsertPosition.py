"""Intuition
The array is sorted, so binary search can be used to find the target or determine where it should be inserted efficiently.

Approach
Used binary search:

Set left and right pointers.
Calculate the middle index.
If the middle element equals the target, return the index.
If the target is greater, move left pointer to mid + 1; otherwise, move right pointer to mid - 1.
If not found, return the left pointer, which is the correct insertion point.

Complexity
Time Complexity
O(logn) (binary search).
Space complexity:
O(1) (constant space).
Code"""

class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
        
