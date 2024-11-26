def main():
    number = int(input("Enter number: "))

    print(square(number))


def hello(name = "World"):
    print("hello,", name)

def square(number):
   return number*number
  
main()