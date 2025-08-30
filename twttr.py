def main():
    x = input("Input: ")
    print(shorten(x))

def shorten(word):
    vowel = "AEIOUaeiou"
    y = ""
    for i in word:
        if vowel.find(i) == -1:
            y += i
    return y


if __name__ == "__main__":
    main()
