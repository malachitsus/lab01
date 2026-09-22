
def tokenize (x):
    token_list = []
    number = ''
    for i in range(len(x)):
        if x[i].isdigit() or x[i] == '.':
            number += x[i]
            if i + 1 == len(x) or not (x[i+1].isdigit() or x[i+1] == '.'):
                token_list.append(float(number))
                number = ''
        elif x[i] in '+-*/()':
            token_list.append(x[i])
            
        elif x[i].isspace():
            continue
        else:
            raise ValueError(f"Неизвестный символ: {x[i]}")
    return token_list

print(tokenize('2+2  *  22.987'))

