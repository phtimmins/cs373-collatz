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


#Caches previously found cycle lengths, 
#both for recursive calls and others top-level calls to cyclelength()
cache = {}

# ------------
# cycle_length 
# ------------
def cycle_length (n) :
    """
    n an integer greater than or equal to 1
    computes the length of the collatz sequence starting with n
    """
    assert n >= 1
   
    # if n is in cache don't do any computing just return 
    if n in cache:
        return cache[n]

    if n == 1:
        length = 1
    elif n % 2 == 0:
        length = 1 + cycle_length(n // 2)
    else:
        length = 2 + cycle_length(n + (n >> 1) + 1)
        
    assert length >= 1

    # set cache with new value
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
