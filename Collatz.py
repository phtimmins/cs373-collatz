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
    


MAX_INT = 2**32 - 1

cache = []


def fillInsert(aList, index, item):
    if index <= len(aList):
        aList[index - 1] = item
    else:
        for i in range(len(aList) + 1, index):
            aList.append(0)
        aList.append(item)




def cycle_length (n) :
    assert n >= 1

    if n > MAX_INT:
        n %= MAX_INT
    assert n <= MAX_INT

    if n <= len(cache) and cache[n - 1] != 0:
        return cache[n - 1]

    if n == 1:
        length = 1
    elif n % 2 == 0:
        length = 1 + cycle_length(n // 2)
    else:
        length = 1 + cycle_length(3*n + 1)
        

    assert length >= 1

    fillInsert(cache, n, length)
    return length

            
    


"""

def cycle_length (n) :
    assert n >= 1

    if n > MAX_INT:
        n %= MAX_INT
    assert n <= MAX_INT

    length = 1

    k = n
    while k != 1:
        if k in cache:
            length += (cache[k] - 1)
            break
        if k % 2 == 0:
            k //= 2
        else:
            k = (3 * k + 1)
        length += 1

    assert length >= 1

    cache[n] = length
    return length
            
"""  

           
    

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
