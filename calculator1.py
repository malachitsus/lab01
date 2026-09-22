
def tokenize (x):
    token_list = []
    number = ''
    for i in range(len(x)):
        if x[i].isdigit() or x[i] == '.':
            number += x[i]
            if i + 1 == len(x) or not (x[i+1].isdigit() or x[i+1] == '.'):
                token_list.append(float(number))
                number = ''
        elif x[i] in '+-':
            if not token_list or (isinstance(token_list[-1], str) and token_list[-1] in '+-*/('):
                if x[i] == '-':
                    number = '-'
            else:
                token_list.append(x[i])
        elif x[i] in '*/()':
            token_list.append(x[i])
        elif x[i].isspace():
            continue
        else:
            raise ValueError(f"Неизвестный символ: {x[i]}")
    return token_list

print(tokenize('-2+2*-22.987'))

def to_rpn (token_list):
    output = []
    stack = []
    PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2}

    for token in token_list:
        if isinstance(token, float):
            output.append(token)
        elif token in '+-*/':
            while stack and stack[-1] != '(' and PRIORITY[stack[-1]] >= PRIORITY[token]:
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
    while stack:
        output.append(stack.pop())

    return output

print(to_rpn([-2.0, '+', 2.0, '*', -22.987]))

def eval_rpn (output):
    stack = []
    for token in output:
        if isinstance(token, float):
            stack.append(token)
        elif token in '+-*/':
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
    return stack[0]

print(eval_rpn([-2.0, 2.0, -22.987, '*', '+']))
