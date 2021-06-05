import grammar.subject as subject
import grammar.noun as noun
import grammar.verb as verb

def analyzer(sentence):
    tokens = sentence.lower().split()
    tokens.append('EOS')

    non_terminals = ['S', 'SB', 'VB', 'NN']
    terminals = [
        'mbah', 'mbak', 'mbek', 'mbok', 'bakiak', 'brem', 
        'bacem', 'becak', 'maca', 'mangan', 'takon', 'tumbas'
    ]

    parse_table = {}
    
    # Non Terminal S
    parse_table[('S', 'mbah')] = ['SB', 'VB', 'NN']
    parse_table[('S', 'mbak')] = ['SB', 'VB', 'NN']
    parse_table[('S', 'mbek')] = ['SB', 'VB', 'NN']
    parse_table[('S', 'mbok')] = ['SB', 'VB', 'NN']
    parse_table[('S', 'bakiak')] = ['error']
    parse_table[('S', 'brem')] = ['error']
    parse_table[('S', 'bacem')] = ['error']
    parse_table[('S', 'becak')] = ['error']
    parse_table[('S', 'maca')] = ['error']
    parse_table[('S', 'mangan')] = ['error']
    parse_table[('S', 'takon')] = ['error']
    parse_table[('S', 'tumbas')] = ['error']
    parse_table[('S', 'EOS')] = ['error']

    # Non Terminal SB
    parse_table = subject.parse_table(parse_table)

    # Non Terminal VB
    parse_table = verb.parse_table(parse_table)

    # Non Terminal NN
    parse_table = noun.parse_table(parse_table)

    stack = []
    stack.append('#')
    stack.append('S')

    token = 0
    symbol = tokens[token]

    while(len(stack) > 0):
        top = stack[len(stack)-1]

        print(f'Top    = {top}')
        print(f'Symbol = {symbol}')

        if top in terminals:
            if top == symbol:
                stack.pop()
                token += 1
                symbol = tokens[token]

                if symbol == 'EOS':
                    print('Isi Stack :', stack)
                    stack.pop() 
            else:
                print('error')
                break
        elif top in non_terminals:
            if parse_table[(top, symbol)][0] != 'error':
                stack.pop()
                push = parse_table[(top, symbol)]

                for i in range(len(push)-1, -1, -1):
                    stack.append(push[i])
            else:
                print('error')
                break
        else:
            print('error')
            break

        print(f'Isi Stack : {stack} \n')        
    
    if symbol == 'EOS' and len(stack) == 0:
        print(f'Input string {sentence}, diterima sesuai Grammar')
    else:
        print(f'Input string {sentence}, tidak diterima, tidak sesuai Grammar')