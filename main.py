import random


# generates random characters
def genCharacter(how_many):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    genLetters = ""
    for choice in range(how_many):
        genLetters += random.choice(letters)
    return genLetters


# generates random numbers
def genNumber(how_many):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    genNumbers = ""
    for choice in range(how_many):
        genNumbers += random.choice(numbers)
    return genNumbers


# generates random symbols
def genSymbol(how_many):
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    genSymbols = ""
    for choice in range(how_many):
        genSymbols += random.choice(symbols)
    return genSymbols


if __name__ == "__main__":
    # requests for user input
    print("===================== My Password Generator ===================")
    charCount = int(input("How many letter do you want in your password: "))
    intCount = int(input("How many numbers do you want in your password: "))
    speCharCount = int(input("How many special characters do you want in your password: "))

    # initializing password string so I can add string to it
    password = ""

    # generating random content
    password += genCharacter(charCount)
    password += genNumber(intCount)
    password += genSymbol(speCharCount)

    # casting the string to a list, so I can shuffle it
    break_pass = list(password)

    # shuffling the content
    random.shuffle(break_pass)

    # casting the list back to string
    password = "".join(break_pass)

    print(f"Your generated password is {password}")
    # this is just a test
