import sys

#What's this code is doing?
#Well, sys is the library which let us handle the command line arguments. 

if len(sys.argv) < 2:
    sys.exit("too few arguments!")

# the syntax I defines here "sys.argv[1:]" it means list is going to start from the index 1 not 0. 
for arg in sys.argv[1:]:
    print("My name is",arg)