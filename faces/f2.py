from dataclasses import replace


def main():
    msg = input("choise :) or :(")

    result = convert(msg)
    
    print(result)

def convert(msg):
    msg1 = msg.replace(":)","😺")
    msg2 = msg1.replace(":(","😿")

    return(msg2)


main()