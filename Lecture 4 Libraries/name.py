import sys

#What's this code is doing?
#Well, sys is the library which let us handle the command line arguments. 

if len(sys.argv) < 2:
    print("too few arguments!")
elif len(sys.argv) > 2:
    print("too many arguments!")
else: print("hello, my name is",sys.argv[1])