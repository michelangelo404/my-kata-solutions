#Convert integer to Whitespace format

def whitespace_number(n):
    if n == 0:
        return ' \n'
    result = ''
    
    b = str(bin(abs(n))[2:])
    for d in b:
        if d == '0':
            result += ' '
        else:
            result += '\t'
    
    return ' ' + result + '\n' if n >= 0 else '\t' + result + '\n'