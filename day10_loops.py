# Iterate 0 to 10 using for loop, do the same using while loop.


# for number in range(11):
    # print(number)


number = -1

while number < 10:
    number += 1
    print(number)

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for a in range(7):
    for x in range(a + 1):
        print("@ ", end="")
    print("\n")

# Use nested loops to create the following:
print("Star square pattern: ")
for a in range(8):
    for x in range(8):
        print("@ ", end="")
    print('\n')