'''
520. Detect Capital
Solved
Easy
Topics
premium lock icon
Companies
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
 

Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
'''


'''
Problem #520: Detect Capital
Conceptual Thinking: Run a single conditional statement with 3 cases:
1. first letter is capitalized, rest are lowercase
2. all letters are capitalized
3. all letters are lowercase
if one of the above conditions are met return true, otherwise return false
'''
# detects if word has proper use of capital letters
def detectCapitalUse(word):
    # checks for 3 cases:
    # 1. first letter is capitalized, rest are lowercase
    # 2. all letters are capitalized
    # 3. all letters are lowercase
    if (word[0].isupper() and word[1:].islower()) or (word[:].isupper()) or (word[:].islower()):
        return True # returns true if conditions are met
    else:
        return False # returns false if conditions not met
    
# Test Cases
print(detectCapitalUse("USA"))
print(detectCapitalUse("FlaG"))