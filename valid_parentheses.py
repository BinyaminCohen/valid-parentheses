# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
#
# Input: s = "()"
# Output: true
# Example 2:
#
# Input: s = "()[]{}"
# Output: true
# Example 3:
#
# Input: s = "(]"
# Output: false

import re

class ValidParentheses(object):
    def is_valid(self, s):

        pattern = r"[(){}\[\]]"
        if bool(re.search(pattern, s)):

            brackets_stack = []
            brackets_map = {')': '(', '}': '{', ']': '['}

            for bracket in s:

                if bracket in brackets_map.values():
                    brackets_stack.append(bracket)

                elif bracket in brackets_map.keys():
                    if not brackets_stack or brackets_stack.pop() != brackets_map[bracket]:
                        return False

            return not brackets_stack

        else:
            print("The string are not contain any of brackets.")
            return False


print(ValidParentheses.is_valid(ValidParentheses, '()[]{}'))
