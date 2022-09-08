# While nice
while True():
    # Get user's input
    fuel = input("Fraction: ")
    try:
        # Try to split the fuel 
        numerator, denominator = fuel.split("/")
        # Convert into integer 
        new_numerator = int(numerator)
        new_denominator =int(denominator)