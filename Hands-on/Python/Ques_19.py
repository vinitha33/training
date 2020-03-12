# Parenthesis Validation

def valid_pare(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif s == ')':
            try:
                stack.pop()
            except:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


string1 = "[{()}]"
print(valid_pare(string1))
