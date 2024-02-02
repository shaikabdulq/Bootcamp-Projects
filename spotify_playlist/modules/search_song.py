# Function to make API call to search one song and get its URI

import requests
import json

def search_song(song, token):
    url = 'https://api.spotify.com/v1/search'
    params = {"q": song, "type": "track", 'market': "IN"}
    response = requests.get(url, params=params, headers={'Authorization': f"Bearer {token}"})
    json_text = (response.text)
    json_data = json.loads(json_text)

    return {"name":(json_data['tracks']["items"][0]['name']),
            "uri":(json_data['tracks']["items"][0]['uri'])}
