def add_songs(*args):
    songs = {}
    result = []
    for data in args:
        song = data[0]
        lyrics = data[1]
        if song not in songs:
            songs[song] = []
        songs[song].extend(lyrics)

    for curr_song, curr_lyric in songs.items():
        result.append(f'- {curr_song}')
        if curr_lyric:
            result.extend(curr_lyric)

    return "\n".join(result)


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
