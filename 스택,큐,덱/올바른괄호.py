def solution(s):
    stk = []
    for char in s:
        if not stk:
            stk.append(char)
        elif stk[-1] == '(' and char == ')':
            stk.pop()
        else:
            stk.append(char)

    if stk:
        return False
    else:
        return True