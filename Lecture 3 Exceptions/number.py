def main():
    print("x is:",get_int("what's x? "))

def get_int(message):
    while True:
        #try will run the instruction will check if there are any exceptions
        try:
            x = int(input(message))
            return x
        #except will catch that exception and let us handle what we want to do with the particular exception
        except:
            pass #it will just pass the exception and follow the code instructions. 

main()