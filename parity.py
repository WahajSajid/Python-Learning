def main():
    n = int(input("Enter number: "))
    if isEven(n):
        print("Even")
    else:
        print("Odd")

def isEven(n):
   return n%2 ==0

main()
