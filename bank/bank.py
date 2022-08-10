#Get User's imput
answer = input("Gretting: ").strip().lower()

#Chek if the answer has "hello" , print $0
if 'hello' in answer:
    print("$0")

# Check if answer stars with 'h', print $20
elif 'h' == answer[0]:
    print("$20")

# Otherwise, print $100
else:
    print("$100")