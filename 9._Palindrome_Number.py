"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp =x
        rev =0
        while(x>0):
            dig=x%10
            rev =rev*10+dig
            x=x//10
        if temp==rev:
            return True
        else:
            return False

   