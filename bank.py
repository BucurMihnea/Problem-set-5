def main():
    x = input("Your greeting: ")
    print(value(x))

def value(greeting):
    if greeting.lower().find("hello", 0, 5) != -1:
        return "$0"
    elif greeting[0].lower() == "h":
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
