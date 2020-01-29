def parseTernary(expression):
    stack = []
    for c in reversed(expression):
        stack.append(c)
        if stack[-2:-1] == ['?']:
            stack[-5:] = stack[-3 if stack[-1] == 'T' else -5]
    return stack[0]
    
if __name__ == "__main__":
    expression = "F?1:T?4:5"
    print(parseTernary(expression))