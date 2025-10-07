'''
2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
Medium
Topics
premium lock icon
Companies
Hint
A critical point in a linked list is defined as either a local maxima or a local minima.

A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].

 

Example 1:


Input: head = [3,1]
Output: [-1,-1]
Explanation: There are no critical points in [3,1].
Example 2:


Input: head = [5,3,1,2,5,1,2]
Output: [1,3]
Explanation: There are three critical points:
- [5,3,1,2,5,1,2]: The third node is a local minima because 1 is less than 3 and 2.
- [5,3,1,2,5,1,2]: The fifth node is a local maxima because 5 is greater than 2 and 1.
- [5,3,1,2,5,1,2]: The sixth node is a local minima because 1 is less than 5 and 2.
The minimum distance is between the fifth and the sixth node. minDistance = 6 - 5 = 1.
The maximum distance is between the third and the sixth node. maxDistance = 6 - 3 = 3.
Example 3:


Input: head = [1,3,2,2,3,2,2,2,7]
Output: [3,3]
Explanation: There are two critical points:
- [1,3,2,2,3,2,2,2,7]: The second node is a local maxima because 3 is greater than 1 and 2.
- [1,3,2,2,3,2,2,2,7]: The fifth node is a local maxima because 3 is greater than 2 and 2.
Both the minimum and maximum distances are between the second and the fifth node.
Thus, minDistance and maxDistance is 5 - 2 = 3.
Note that the last node is not considered a local maxima because it does not have a next node.
 

Constraints:

The number of nodes in the list is in the range [2, 105].
1 <= Node.val <= 105
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution
def nodesBetweenCriticalPoints(head):
    # variables to track prev/cur nodes, indexes of all critical points, and the current index
    prev = head
    cur = prev.next
    critical_points = []
    i = 0
    # iterates through LL finding all critical points
    while cur != None:
        if cur.next != None:
            # checks for critical points
            if (cur.val < prev.val and cur.val < cur.next.val) or (cur.val > prev.val and cur.val > cur.next.val):
                critical_points.append(i) # adds critical point to list
        # update prev/cur nodes and cur index
        prev = cur
        cur = cur.next
        i += 1
    # return [-1, -1] or edge case (< 2 critical vals)
    if len(critical_points) < 2:
        return [-1,-1]
    # compare differences of indexes that are adjacent in critical_points and find min 
    minDistance = critical_points[1] - critical_points[0] # start minDistance with first adjacent pair
    # iterate through critical points finding lowest difference of adjacent points
    for index, point in enumerate(critical_points):
        # checks index is in range
        if index + 1 < len(critical_points):
            # updates minDistance if applicable
            if (critical_points[index + 1] - critical_points[index]) < minDistance:
                minDistance = critical_points[index + 1] - critical_points[index]
    # compares first and last indexes of critical points to find max distance
    maxDistance = critical_points[len(critical_points) - 1] - critical_points[0]
    # returns min/max distance between critical points in an array
    return [minDistance, maxDistance]

# Test Cases
linked_list1 = ListNode(3, ListNode(1, None))
linked_list2 = ListNode(5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2, None)))))))
linked_list3 = ListNode(1, ListNode(3, ListNode(2, ListNode(2, ListNode(3, ListNode(2, ListNode(2, ListNode(2, ListNode(7, None)))))))))
print(nodesBetweenCriticalPoints(linked_list1)) # expected ([-1, -1])
print(nodesBetweenCriticalPoints(linked_list2)) # expected ([1, 3])
print(nodesBetweenCriticalPoints(linked_list3)) # expected ([3, 3])