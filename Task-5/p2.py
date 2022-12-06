
def valid(ip):
    stack = []

    for char in ip:
        if char in ["(", "{", "["]:

            stack.append(char)
        else:

            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if stack:
        return False
    return True


ip = input()
if valid(ip):
    print("true")
else:
    print("false")

