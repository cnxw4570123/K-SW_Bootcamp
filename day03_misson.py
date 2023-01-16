song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!
"""

song_list = song.split()
for i in range(len(song_list)):
    if song_list[i].startswith('m'):
        song_list[i] = song_list[i].replace('m', 'M')
print(' '.join(song_list))