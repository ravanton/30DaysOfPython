# Create list with the name of all months
months =     [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# Loop forever
while True:
    #  Get user input
    date = input("Date: ")
    try:
        # Split the date by /
       month, day, year = date.split("/")
       # Check if month is in between of 1 and  12 and day between 1 and 1
       if( int(month) >= 1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31 ):
        break
    except:
        try:
            # Split  the day by space 
            old_month, old_day, old_year = date.split(" ")
            # Find  the number of the month 
            for i in range(len(months)):
                
            