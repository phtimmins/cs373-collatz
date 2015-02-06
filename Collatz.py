#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert i >= 1
    assert j >= 1

    if i > j:
        i, j = j, i

    assert i <= j

    result = max(cycle_length(x) for x in range(i, j + 1))
    assert result >= 1
    return result


cache = {}
"""
MAX = 2**31 - 1
def cyc (n) :

    if n in cache:
        return cache[n]

    if n == 1:
        length = 1
        toBig = False
        
    elif n % 2 == 0:
        subLen, childToBig = cyc(n // 2)
        length = subLen + 1
        toBig = n > MAX or childToBig
    else:
        subLen, childToBig = cyc(3*n + 1)
        length = subLen + 1
        toBig = n > MAX or childToBig
        
    cache[n] = (length, toBig)
    return (length, toBig)

def run_all():
    for i in range(1, 1000000):
        length, toBig = cyc(i)
        if toBig:
            yield i



toBig  = [i for i in run_all()]

import random
random.seed(3434)

def bounds():

    tooBig  = [i for i in toBig]
    for i in range(0, 100):
        i = tooBig.pop(0) 
        j = tooBig.pop(0) 

        i += 1
        j -= 1

        if i >= j:
            continue

        l = random.randint(i+1, j-1) 
        r = random.randint(i+1, j-1) 
        yield (l, r) 
    
bou = [i for i in bounds()]
bou.append((1,1))
bou.append((999789, 999999))


def verify(): 
    sett = {i for i in toBig}
    for pair in bou:
        print(str(pair[0]) + " " + str(pair[1]))
        for j in range(pair[0], pair[1] + 1):
            if j in sett:
                return False

    for pair in bou:
        print(str(pair[1]) + " " + str(pair[0]))
        for j in range(pair[0], pair[1] + 1):
            if j in sett:
                return False

    return True
"""            

  
def cycle_length (n) :
    assert n >= 1

    if n in cache:
        return cache[n]

    if n == 1:
        length = 1
    elif n % 2 == 0:
        length = 1 + cycle_length(n // 2)
    else:
        length = 2 + cycle_length(n + (n >> 1) + 1)
        
    assert length >= 1
    cache[n] = length
    return length

           
# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
