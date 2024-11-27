def main():
    n = get_number()
    meow(n)

def meow(n):
    for _ in range(n):
        print("meow")

def get_number():
    message = "What's n? "
    while True:
       n = int(input(message))
       if n<0:
           message = "Number can't be negative! Enter again: "
           continue
       else: return n


main()