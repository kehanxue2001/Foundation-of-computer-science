# Assume that the argument D is a dictionary whose keys and values
# are all integers. Assume that the argument n is an integer.
#
# Returns the longest strictly increasing list of integers
# of the form [n, D[n], D[D[n]], D[D[D[n]]], ...]
# provided n is one of D's keys.

def f4(D, n):
    if n not in D:
        return []
    else:
        L=[n]
    while n in D and n<D[n]:
        L.append(D[n])
        n=D[n]
    return L
    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE
