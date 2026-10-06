# Калькулятор:

# 1) Токенизация: разбиение выражения на токены

'''Разбивает строку выражения на список токенов.

    Args:
        x: Строка с математическим выражением.

    Returns:
        Список токенов, где числа представлены как float,
        а операторы и скобки - как строки.

    Raises:
        ValueError: Если во входной строке встречается недопустимый символ.
'''

def tokenize (x):
    x = x.replace(' ', '')
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

'''
    Проверяет список токенов на логические и синтаксические ошибки.

    Args:
        token_list: Список токенов, полученный после токенизации.

    Returns:
        None. Функция только валидирует выражение.

    Raises:
        ValueError: Если выражение пустое, начинается с оператора,
            заканчивается не числом или скобкой, содержит два оператора
            подряд, два числа подряд или несбалансированные скобки.
'''

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

'''Преобразует список токенов в обратную польскую запись (RPN).

    Args:
        token_list: Валидный список токенов инфиксного выражения.

    Returns:
        Список токенов в порядке обратной польской записи.
'''
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

'''
    Вычисляет значение выражения, записанного в обратной польской записи.

    Args:
        output: Список токенов в формате RPN.

    Returns:
        Результат вычисления выражения как число (float).

    Raises:
        ValueError: При делении на ноль или взятии остатка по нулю.
'''
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
'''Вычисляет значение математического выражения.

    Args:
        expr: Строка с математическим выражением
            (поддерживаются числа, +, -, *, /, %, скобки).

    Returns:
        Результат вычисления выражения как число (float).

    Raises:
        ValueError: При недопустимых символах, синтаксических ошибках,
            несбалансированных скобках или делении на ноль.
'''
def calculate(expr):
    tokens = tokenize(expr)
    validate(tokens)
    rpn = to_rpn(tokens)
    return eval_rpn(rpn)



