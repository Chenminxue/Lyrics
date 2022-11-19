import lyrics_generator

###########################################################
#                                                         #
#                   Input song name                       #
#                                                         #
###########################################################
def input_song_name():

    song_name = input("Please type the song name: ")

    return song_name




if __name__ == "__main__":

    web_searcher = lyrics_generator.Lyrics_Generator(input_song_name())
    songid = 1979068123
    web_searcher.lyrics_search(songid)
    web_searcher.songid_search()