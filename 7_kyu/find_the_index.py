#Find the index of the second occurrence of a letter in a string

def second_symbol(s, symbol):
    if s.count(symbol) <= 1: return -1
    cnt = 0
    for c,i in enumerate(s):
        if i == symbol:
            cnt += 1
        if cnt == 2:
            return c
            
            