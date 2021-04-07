def recite(start, take=1):
    full_song = create_song()
    output = []
    for i in range(2*(start+1), 2*(start+1-take), -1):
        output.append(full_song[200-i])

    if len(output) > 2:
        count = 0
        for i in range(len(output)):
            if i % 2 == 0 and i > 1:
                output.insert(i + count, "")
                count += 1
    return(output)


def create_song():
    song = []

    for i in range(100):
        if i == 98:
            left_on_wall = "no more bottles"
        elif i == 97:
            left_on_wall = f"{98 - i} bottle"
        else:
            left_on_wall = f"{98 - i} bottles"

        if i == 99:
            song.append(
                f"No more bottles of beer on the wall, no more bottles of beer.")
            song.append(
                f"Go to the store and buy some more, 99 bottles of beer on the wall.")
        elif i == 98:
            song.append(
                f"{99-i} bottle of beer on the wall, {99-i} bottle of beer.",)
            song.append(
                f"Take it down and pass it around, {left_on_wall} of beer on the wall.")
        else:
            song.append(
                f"{99-i} bottles of beer on the wall, {99-i} bottles of beer.",)
            song.append(
                f"Take one down and pass it around, {left_on_wall} of beer on the wall.")
    return song
