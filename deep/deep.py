# Get User input
answer = input("What's the answer to the Greate Question of Life, the Universe and Everthing? ").strip().lower()
# Print "Yes" if the user inputs 42 or (case-insensityvety) forty-two or forty two 
if answer == "42":
    print("Yes")
elif answer == "forty-two":
    print("Yes")
elif answer == "forty two":
    print("Yes")
# Otherwise output No
else:
    print("No")