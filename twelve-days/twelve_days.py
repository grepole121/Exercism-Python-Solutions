nth = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eigth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth"
}

gifts = [
    "a Partridge in a Pear Tree.",
    "two Turtle Doves, ",
    "three French Hens, ",
    "four Calling Birds, ",
    "five Gold Rings, ",
    "six Geese-a-Laying, ",
    "seven Swans-a-Swimming, ",
    "eight Maids-a-Milking, ",
    "nine Ladies Dancing, ",
    "ten Lords-a-Leaping, ",
    "eleven Pipers Piping, ",
    "twelve Drummers Drumming, "
]


def recite(start_verse, end_verse):
    for i in range(start_verse,end_verse+1):
        print(f"\nOn the {nth[i]} day of Christmas my true love gave to me: ", end = '')
        for gift in range (0,i):
            if(i-gift == 1) and (i != 1):
                print("and ", end = '')
            print(f"{gifts[i-gift-1]}", end = '')
    return
