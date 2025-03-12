# Assume that the argument filename is the name of a text file
# that exists in the working directory, and
# that the file consists of lines of the form
# first_name,count_in_thousands
#
# The output is printed out, not returned.

def f5(filename):
    with open(filename) as file:
        for line in file:
            name, count=line.split(',')
            print(int(count)*1000,'people named',name)
    # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE
