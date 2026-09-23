# Калькулятор:

# 1) Токенизация: разбиение выражения на токены
def tokenize (x):
    token_list = []
    number = ''
    for i in range(len(x)):
        if x[i].isdigit() or x[i] == '.':
            number += x[i]
            if i + 1 == len(x) or not (x[i+1].isdigit() or x[i+1] == '.'):
                token_list.append(float(number))
                number = ''
        elif x[i] in '+-': # Унарный +/-: если токен-лист пуст, или предыдущий токен — оператор/скобка
            if not token_list or (isinstance(token_list[-1], str) and token_list[-1] in '+-*/('): 
                if x[i] == '-':
                    number = '-'
            else:
                token_list.append(x[i])
        elif x[i] in '*/%()':
            token_list.append(x[i])
        elif x[i].isspace():
            continue
        else: # Валидация недопустимых символов
            raise ValueError(f"Unknown symbol: {x[i]}")
    return token_list

# 2) Валидация: проверка недопустимых значений и логических ошибок
def validate (token_list):
    if not token_list: 
        raise ValueError('Symbols not found')
    
    if isinstance(token_list[0], str) and token_list[0] in '+-*/%':
        raise ValueError('Invalid operation syntax')
    
    if not isinstance(token_list[-1], float) and token_list[-1] != ')':
        raise ValueError('Last element lost')
    
    for i in range(len(token_list) - 1):
        a = token_list[i]
        b = token_list[i+1]
        if (isinstance(a, str) and a in '+-*/%' 
            and isinstance(b, str) and b in '+-*/%'):
                raise ValueError('Invalid operation')
        if isinstance(a, float) and isinstance(b, float):
            raise ValueError('Invalid operation')
    balance = 0  # Баланс скобок: на каждую '(' должна быть ')'
    for token in token_list:
        if token == '(':
            balance += 1
        elif token == ')':
            balance -= 1
            if balance < 0:
                raise ValueError('Unbalanced )')
    if balance > 0:
        raise ValueError('Unbalanced (')
    
    

# 3) Преобразование в RPN (shunting-yard)
def to_rpn (token_list):
    output = []
    stack = []
    PRIORITY = {'+': 1, '-': 1, 
                '*': 2, '/': 2, 
                '%': 2}

    for token in token_list:
        if isinstance(token, float):
            output.append(token)
        elif token in '+-*/%':
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

# 4) Вычисление RPN через стек
def eval_rpn (output):
    stack = []
    for token in output:
        if isinstance(token, float):
            stack.append(token)
        elif token in '+-*/%':
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/': # Здесь валидация делителя: запрещён 0
                if b == 0:
                    raise ValueError('Zero division')
                else:
                    stack.append(a / b)
            elif token == '%':
                if b == 0:
                    raise ValueError('Zero division')
                else:
                    stack.append(a % b)            
                 
    return stack[0]

# 5) Общая функция
def calculate(expr):
    tokens = tokenize(expr)
    validate(tokens)
    rpn = to_rpn(tokens)
    return eval_rpn(rpn)



