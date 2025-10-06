'''
1493. Longest Subarray of 1's After Deleting One Element
Medium
Topics
premium lock icon
Companies
Hint
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

# This functions iterates through the array while maintaining a range on indexes that exist between 0's to find the longest subarray of 1's
def longestSubarray(nums) -> int:
    numZeroes = 0   # tracks # of 0's
    longestSubArrLen = 0   # tracks the longest subarray of 1's between 0's
    start = 0   # tracks start position
    # iterates through array creating/tracking a range of indexes where the end values are 0
    for i, num in enumerate(nums):
        # prepare to move index range when 0 is found
        if num == 0: 
            numZeroes += 1
        # move index range so each end contains a 0
        while numZeroes > 1:
            if nums[start] == 0: numZeroes -= 1
            start += 1
        # update longest subarray length if new range is longer
        if i-start > longestSubArrLen:
            longestSubArrLen = i-start
    # returns length of the longest subarray of 1's
    return longestSubArrLen   

print(longestSubarray([1,1,0,1]))
print(longestSubarray([0,1,1,1,0,1,1,0,1]))
print(longestSubarray([1,1,1]))