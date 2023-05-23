#Car Number Plate Calculator

import math as m

def find_the_number_plate(cid):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    #calculates the number of times cid will cause letters to change
    exc = m.floor(cid/999)
    
    #letter progression counters
    subcount1 = 0
    subcount2 = 0
    sn=str(cid%999+1)
    #this loop starts when the third letter needs to be changed at least once
    while exc > 676:
        exc -= 676
        subcount2 +=1
    while exc >= 26:
        exc -= 26
        subcount1 += 1
    while len(sn) < 3:
        sn = '0' + sn
    return alph[exc]+alph[subcount1]+alph[subcount2]+sn

