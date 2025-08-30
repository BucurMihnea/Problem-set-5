def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    punct = " ,.:;!?"
    if len(s) < 2 or len(s) > 6:
        return False
    elif s[0].isalpha() == 0 or s[1].isalpha() == 0:
        return False
    else:
        for i in range(len(s)):
            if punct.find(s[i]) != -1 or (s[i].isalpha() and s[i-1].isnumeric() and i > 0) or (s[i-1].isalpha() and s[i] == "0" and i > 0):
                return False
    return True


if __name__ == "__main__":
    main()
