# While nice
while True:
    # Get user's input
    fuel = input("Fraction: ")
    try:
        # Try to split the fuel 
        numerator, denominator = fuel.split("/")
        # Convert into integer 
        new_numerator = int(numerator)
        new_denominator =int(denominator)
        # Calculat the percentage
        f = new_numerator / new_denominator
        # Check if it less than 1 stop the loop 
        if f <= 1:
            break 
    except(ValueError, ZeroDivisionError):
        pass
# Multiply percentage by 100
p = int(f * 100)
# Check if percentage is less than 1, print E
if p <= 1:
    print("E")
# Check if percentage is greater  than 99, print F
elif p >= 99:
    print("F")
# Otherwise, print the %
else: print(f"{p}%")