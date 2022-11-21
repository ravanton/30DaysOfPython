autumn = ("September", "October", "November")
winter =("December", "January", "February")
spring = ("March", "April", "May")
summer =("June", "July", "August")

season = input("Enter season: ").title()
if season in autumn:
    print(" is Autumn")
elif season in winter:
    print( "is Winter ")
elif season in spring:
    print("is Spring")
else:
    print(" is Summer")