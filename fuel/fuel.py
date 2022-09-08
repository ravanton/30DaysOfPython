# While nice
while True():
    # Get user's input
    fuel = input("Fraction: ")
    try:
        # Try to split the fuel 
        numerator, denominator = fuel.split("/")