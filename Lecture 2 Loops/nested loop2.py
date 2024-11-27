def main():
    square(3)

def square(length):
    for i in range(length):
        for j in range(length):
            print("?",end = "")
        print("\n",end="")

main()