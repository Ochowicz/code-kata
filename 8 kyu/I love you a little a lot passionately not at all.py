def how_much_i_love_you(nb_petals):
    phrases = {1: "I love you",2: "a little", 3:"a lot", 4:"passionately", 5:"madly", 6:"not at all"}
    return phrases[(nb_petals - 1) % 6 + 1]