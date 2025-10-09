'''
2. Add Two Numbers
Solved
Medium
Topics
premium lock icon
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Problem #2: Add Two Numbers (Medium)
Conceptual Idea: iterate through both LL finding the 2 addends, sum them together, convert to a string and iterate through the string to create a LL
Problems Encountered: at first when I tried using integers it wouldn't work for numbers too large so I converted the sum to a string before creating the LL
'''
def addTwoNumbers(l1, l2):
    cur = l1
    digit = 1
    num1 = 0
    # iterate through LL and get first num
    while cur != None:
        num1 += cur.val * digit
        digit *= 10
        cur = cur.next
    cur = l2
    digit = 1
    num2 = 0
    # iterate through LL and get second num
    while cur != None:
        num2 += cur.val * digit
        digit *= 10
        cur = cur.next
    sum = num1 + num2
    sum = str(sum)
    # iterate through string creating a LL to return
    result = None
    pointer = None
    while sum != "":
        curNode = ListNode(int(sum[-1]), None)
        sum = sum[:-1]
        if result is None:
            result = curNode
            pointer = result
        else:
            pointer.next = curNode
            pointer = pointer.next

    return result


# Test Cases
result1 = addTwoNumbers(ListNode(2, ListNode(4, ListNode(3, None))), ListNode(5, ListNode(6, ListNode(4, None))))
result2 = addTwoNumbers(ListNode(5, ListNode(6, ListNode(4, None))), 
                        ListNode(1, ListNode(0,  ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(1, None))))))))))))))))))))))))))))))))
print("breakpoint here")