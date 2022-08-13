def main():
    #Get time from user 
    answer = input("What time is it? ")
    #Call the convert function
    time = convert(answer)
    #Breakfast between 7:00 and 8:00
    if  7 <= time <= 8:
        print("breakfast time")
    #Lunch between 12:00 and 13:00
    if 12 <= time <= 13:
        print("lunch time")
    #Dinner between 18:00 and 19:00
    if 18 <= time <= 19:
        print("dinner time")
def convert(time):
    #Get hour and minute
    hours, minutes = time.split(":")
    #Convert time into a float number
    new_minute = float(minutes) / 60
    # Return the result to main function 
    return float(hours) + new_minute  
if __name__ == "__main__":
    main()
