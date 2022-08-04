from data_structures.stack import Stack


def multi_bracket_validation(my_string):
    braces_stack = Stack()
    for char in my_string:
        if char == ")":
            if not validate_braces(braces_stack, char, 1):
                return False
        elif char == "}" or char == "]":
            if not validate_braces(braces_stack, char, 2):
                return False
        elif char == "(" or char == "{" or char == "[":
            braces_stack.push(char)
    return True


def validate_braces(braces_stack, curr_char, ascii_ref):
    if braces_stack.is_empty():
        return False
    if braces_stack.peek() != chr(ord(curr_char) - ascii_ref):
        return False
    else:
        braces_stack.pop()
        return True
