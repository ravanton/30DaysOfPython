#Make faces
def main():
    #Get User's input
    msg = input("You'r happy or sad? ")
    
    #Call convert function 
    result = convert(msg)
   
    #Print the result 
    print(result)
def convert(msg):
    #Replace :) for happy emoji
    msg_happy = msg.replace(":)", "🙂")
    #Replace :( for sad emoji
    msg_sad = msg_happy.replace(":(", "🙁")
    #Return string
    return msg_sad

main()