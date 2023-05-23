#Are they the "same"?

import math
import copy

def comp(a, b):
    i = 0
    bnew = copy.deepcopy(b)
    
    if a != None and b != None:
        for n in a:
            if n**2 in bnew:
                bnew.remove(n**2)
                i += 1
    
        if i == len(a) and i == len(b):
            return True

        else:
            return False
        
    else:
        return False
	

