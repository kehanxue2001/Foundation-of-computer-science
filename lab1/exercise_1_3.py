# Assume that the argument L is a list of integers.
#
# Removes from L all integers x such that L is of the form
# [..., x, x_1, ..., x_n, e]
# with n >= 0 and x, x_1, ..., x_n all strictly smaller than e.
#
# Use only one loop.
#
# The output is printed out, not returned.

def f3(L):
    while len(L)>1 and L[-2]<L[-1]:
        L.remove(L[-2])
    print(L)
    # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE
