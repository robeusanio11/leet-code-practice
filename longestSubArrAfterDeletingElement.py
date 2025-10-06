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

def longestSubarray(nums) -> int:
    longestSubArr = 0   # longest subarr starts at 0
    # iterate through removing 1 element at a time
    for index, num in enumerate(nums):
        curList = nums.copy()   # copy original arr to new arr
        curList.pop(index)   # remove current element in loop
        curLongest = 0    # set the current longest subarray to 0
        # iterate through new arr checking for longest subarr
        for curNum in curList:
            # add to cur subarr length for each 1 in a row
            if curNum == 1:
                curLongest += 1
            # set the new longest subarr if applicable
            if curLongest > longestSubArr:
                longestSubArr = curLongest
            # reset longest subarr of 1's if 0 is found
            if curNum == 0:
                curLongest = 0

    return longestSubArr   # returns the longest subarr


print(longestSubarray([1,1,0,1]))
print(longestSubarray([0,1,1,1,0,1,1,0,1]))
print(longestSubarray([1,1,1]))