"""
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

..................................

Intuition:
first I used nested loops to check each number by adding with the next, but it was not time efficient, and came across using hashmap.

Approach:
By checking remainder and storing in hashmap.

Time complexity:
O(n)

Space complexity:
12.3 MB

Runtime : 26ms | Beats: 99.40%

Memory :12.29 MB | Beats: 97.83%


Code:
"""
class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i

sol=Solution()

sol.twoSum([10,45,63,2,72,85,50],130)