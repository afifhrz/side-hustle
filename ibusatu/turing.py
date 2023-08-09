def is_valid_brackets(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in ['(', '[', '{']:
            stack.append(char)
        elif char in [')', ']', '}']:
            if not stack or bracket_map[char] != stack.pop():
                return False

    return len(stack) == 0

print(is_valid_brackets(")"))