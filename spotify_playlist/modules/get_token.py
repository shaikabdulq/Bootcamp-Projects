# To get token for Spotify Web API using API key

import requests
def get_token():
    print(f'Calling Spotify API for token ...')
    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type":"client_credentials",
            "client_id":"ENTER_CLIENT_ID",
            "client_secret":"ENTER_CLIENT_SECRET"}
    response = requests.post(url, headers={"Content-Type":"application/x-www-form-urlencoded"}, data=data)
    token = ((response).json().get("access_token"))
    print(f'Token received\n')
    return token