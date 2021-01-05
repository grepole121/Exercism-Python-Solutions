import string


responses = ["Sure.",
             "Whoa, chill out!",
             "Calm down, I know what I'm doing!",
             "Fine. Be that way!",
             "Whatever."]

def response(hey_bob):
    hey_bob = hey_bob.replace(" ","")
    hey_bob = hey_bob.replace("\n","")
    hey_bob = hey_bob.replace("\t","")
    hey_bob = hey_bob.replace("\r","")

    if hey_bob == "":
        return responses[3]
    elif (hey_bob[-1] == "?") and (hey_bob.isupper()):
        return responses[2]
    elif hey_bob.isupper():
        return responses[1]
    elif hey_bob[-1] == "?":
        return responses[0]

    return responses[4]