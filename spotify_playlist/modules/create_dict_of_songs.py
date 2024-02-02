# To create a dict with key as URI and values as [rank, name]
from modules.search_song import search_song

def dict_songs(song_list, token):
    dict = {} # {'uri' : [rank, name]}
    count = 0
    print(f'Searching for songs in Spotify ...')
    for song in song_list:
        song_data = search_song(song,token)
        name = song_data['name']
        uri = song_data['uri']
        dict[uri] = [(count+1),name]
        count +=1
        print(f'{count} songs searched ')
    return dict
