#!coding:utf-8
import requests
import bs4
import json


###########################################################
#                                                         #
#                   Lyrics generator                      #
#                                                         #
###########################################################
class Lyrics_Generator:

    def __init__(self, song_name = None) -> None:
        self.lyrics = None
        self.song_name = song_name

    def songid_search(self):
        url = 'https://music.163.com/'
        try:
            response = requests.get(url)
            status_code = response.status_code
        except:
            print("Sorry, the music platform url is not available!\n\n\n")
        
        content = bs4.BeautifulSoup(response.content.decode("utf-8"), "lxml")
        element = content.find_all(id='song?id')
        print(element)

    def lyrics_search(self, songid):
        url = 'https://music.163.com/api/song/lyric?id=' + str(songid) + '&lv=1&kv=1&tv=-1'

        # Check whether the url is available or not       
        try:       
            response = requests.get(url)
            print(response.status_code)
        except:
            print("Sorry, the api url is not available!\n\n\n")

        lyric = response.text

        json_obj = json.loads(lyric)

        print(json_obj)

        self.lyrics = json_obj['lrc']['lyric']
        
        print(self.lyrics)


    def write_to_txt(self):
        pass
