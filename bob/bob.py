import string

responses = ["Sure.",
             "Whoa, chill out!",
             "Calm down, I know what I'm doing!",
             "Fine. Be that way!",
             "Whatever."]


def response(hey_bob):
    hey_bob = hey_bob.strip()

    if hey_bob == "":
        return responses[3]
    elif ( hey_bob.endswith("?") ) and ( hey_bob.isupper() ):
        return responses[2]
    elif hey_bob.isupper():
        return responses[1]
    elif hey_bob.endswith("?"):
        return responses[0]
    else:
        return responses[4]