# Get user input
answer = input("Input: ")

# Print "Output: "
print("Output: ", end="")

#Loop through every letter
for letter in answer:
    # Chek if it is not vowels whether inputed in upper case or lowercase
    if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:  
        # Print the letter
        print(letter, end="")
#Print new line
print()