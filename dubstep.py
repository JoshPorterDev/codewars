def songdecoder(song):
    newSong = song.replace('wub', ' ')

    return newSong  

test = songdecoder('AWUBWUBWUBBWUBWUBWUBC')
print(test)

# test = 'I like Pie'
# x = test.replace('Pie', 'Cake')
# print(x)