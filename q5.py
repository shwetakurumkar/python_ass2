class ParenthesesValidator:
    def _init_(self):
        self.bracket_map = {')': '(', '}': '{', ']': '['}

    def is_valid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in self.bracket_map:
                top_element = stack.pop() if stack else '#'
                if self.bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

validator = ParenthesesValidator()
test_strings = ["()", "()[]{}", "[)", "({[]})", "{{{"]
for test in test_strings:
    print(f"{test}: {'Valid' if validator.is_valid(test) else 'Invalid'}")