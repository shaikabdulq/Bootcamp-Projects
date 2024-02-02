# To get a list of top 100 songs as per rank in ascending order
import requests
from bs4 import BeautifulSoup

def songs_list():
    print(f"Fetching list of top 100 songs ...")
    url = "https://entertainment.expertscolumn.com/100-greatest-bollywood-love-songs-of-the-2000s"
    html = (requests.get(url)).text
    # print(html)
    soup = BeautifulSoup(html,'html.parser')

    song_list = []
    for item in (soup.find(name="div",class_="blog-single-details").find(name="ol").find_all("li")):
        song_list.append(item.string.strip())
    # print(song_list)
    print(f'Fetching successful\n')
    return song_list
