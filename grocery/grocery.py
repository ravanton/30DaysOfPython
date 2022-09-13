# Create empty dicrionary
grocery = {}
# Loop forever 
while True:
    try:
        # Get user input
        item = input()
        # Check if item is already in the dictionary 
        if item in grocery:
            # If it is, add 1 in the count 
            