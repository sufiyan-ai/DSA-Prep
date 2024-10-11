""" Runtime 16 ms
Intuition
Using two pointers allowed me to overwrite elements efficiently, keeping the valid ones at the front of the array.
Complexity:
Time Complexity: O(n) – We traverse the array once.
Space Complexity: O(1) – We modify the array in place without extra space.

Approach
Two Pointers:

One pointer (i) iterates through the array.
Another pointer (k) keeps track of where the next valid element (not val) should go.
Iterate and Replace:

If nums[i] != val, place it at nums[k] and increment k.
Ignore elements equal to val.
Return:
Return k, the count of valid elements.

Complexity
Time Complexity:
O(n)

Space Complexity:
O(1)""""


class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
