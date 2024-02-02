# Python Music Search Project (Spotify Playlist)

## Overview
This project is designed to get a list of top 100 Bollywood songs of 2000s from the website https://entertainment.expertscolumn.com, search and retrieve song information using Spotify API and create a playlist in the user's spotify account.

### Requirements
- Python 3.9
- Required Python packages:
    - BeautifulSoup
    - Spotipy

### API Keys
- Get Client ID and Client Secret using [Spotify API](https://developer.spotify.com)
- Get User ID from Spotify. For detailed instructions on how to get user id, click [here](https://www.businessinsider.com/guides/streaming/how-to-find-spotify-username?IR=T)
- Enter Client ID, Client Secret and User ID in `main.py` 
- Enter Client ID and Client Secret in `module.get_token.py`. 

## Usage

1. **Main Program**: Run `python main.py` to start the main program.
2. **Get songs list**: `songs_list()` gets list of top 100 songs as per rank in ascending order from https://entertainment.expertscolumn.com/100-greatest-bollywood-love-songs-of-the-2000s
3. **Get Spotify API Token**: `get_token()` gets token for Spotify Web API
4. **Search for a Song**: `search_song()` searches for a song in Spotify's Database, using its API, and retrieves URI of the song.
5. **Create Playlist**: An object 'sp', derived from using `Spotify()` class, creates playlist using `sp.user_playlist_create()` and add songs to the playlist using `sp.playlist_add_items()` 

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request.