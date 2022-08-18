def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    #vanity plates may contain a max of 6 characters(letters or numbers)
    # and a min of 2  characters.
    if len(s) < 2 or len(s) > 6:
        return False
    # All vanity plates must start with at least two letter 

    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False 
    # Number cannot be used in the middle of a plate; they must come at the end.
    # for example, AAA222 would be an acceptable _ vanity plate; AAA222 would not be acceptable.
    # The first number used cannot be a '0'
    i = 0
    while i < len(s):
        if s[1].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1
    # No periods, spaces or punctuation marks are allowed
    for c in s:
        if c in ['.', ' ', '!', '?']:
            return False
    # If we pass all the tests, return True
    return True

main()
