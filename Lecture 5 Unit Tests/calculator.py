def main():
    x = int(input("what's x? "))
    squaredX = square(x)
    print("square of x is:",squaredX)

def square(n):
    return n*n


if __name__ == "__main__":
    main()