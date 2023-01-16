song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!
"""

song_list = song.split()
for i in range(len(song_list)):
    if song_list[i].startswith('m'):
        song_list[i] = song_list[i].title()
print(' '.join(song_list))

print('My kitty cat likes %s\n My kitty cat likes %s\n My Kitty cat fell on his %s And now thinks he\'s a %s ' % ('roast beef', 'ham', 'head', 'clam'))
