name = input("What's your name? ")

match name:
    case "Wahaj" | "Maraj" | "Neha":
        print("Wahaj's house")
    case "Ashareb":
        print("Ashareb's hosue")
    case _:
        print("who?")