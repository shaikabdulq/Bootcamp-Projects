# Program to scrap the web to get a list of top 100 bollywood songs of 2000s, search the songs on spotify and create a spotify playlist

import spotipy
from spotipy import SpotifyOAuth
from modules.get_token import get_token
from modules.songs_list import songs_list
from modules.create_dict_of_songs import dict_songs
# from modules.search_song import search_song

# Scrapes the website and gets a list of top 100 songs
song_list = songs_list()

# Retrieves token from Spotify API
token = get_token()

# Creates a list of song URIs
dict_songs = dict_songs(song_list,token) # dict of songs in {"uri" : [rank, "name"]} format
uri_list=[]
for k,v in dict_songs.items():
    uri = k
    uri_list.append(uri)

# Authentication with Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="ENTER_CLIENT_ID",
        client_secret="ENTER_CLIENT_SECRET",
        show_dialog=True,
        cache_path="token.txt"
    )
)

# To create a playlist
playlist_name = 'Top 100 songs of 2000s'
user_id = 'ENTER_USER_ID'
playlist = sp.user_playlist_create(user=user_id, name=f"{playlist_name}", public=False)
print(f'{playlist_name} Playlist created')

# To add songs to playlist
playlist_id = playlist['id']
tracks = sp.playlist_add_items(playlist_id,items=uri_list)
