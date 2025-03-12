# Assume that the argument filename is the name of a text file
# that exists in the working directory, and
# that the file consists of lines that are either blank
# or of the form
#         count symbol
# with count an integer at least equal to 1,
# with at least one space between count and symbol,
# and with possibly spaces before count and after symbol.
#
# The output is printed out, not returned.

def f6(filename):
    with open(filename) as file:
        for line in file:
            if not line.isspace():
                count,symbol=line.split()
                print(int(count)*symbol)
                
                
    # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE
