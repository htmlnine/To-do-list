import random

def handlemessage(message) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return("Hey Daddyy")

    
    if p_message == "random":
        return(random.randInt(1,6))


    if p_message == "!help":
        return "'This is a help message'"