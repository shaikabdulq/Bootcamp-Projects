# Program to scrap the Hacker News website to get the most upvoted article

import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
html = requests.get(url)
html_text = html.text

soup = BeautifulSoup(html_text,'html.parser')
# print(soup.prettify())

# for tag in soup.find_all("a"):
#     print(tag.get("href"))

count = 0
score_list = []
link_list = []
link_text_list = []

# To get a list of all scores in integer form
for tag in soup.find_all(name="span", class_="score"):
    score = int((tag.string.split())[0])
    score_list.append(score)

# To get a list of link_text and link
for tags in soup.find_all(name="span",class_="titleline"):
    if (tags.find("a").get("href")).startswith("https"):
        link_text_list.append(tags.find("a").string)
        link_list.append(tags.find("a").get("href"))

# print(link_text_list)
# print(link_list)
# print(score_list)

# To create a Dictionary where link is the key and [link_text,score] is value
dict = {}
count = 0
while True:
    try:
        dict[(link_list[count])] = [(link_text_list[count]),(score_list[count])]
        count += 1
    except:
        break

# To create a list of [score,link] which is sorted in descending order
list = []
for k,v in dict.items():
    list.append((v[1],k))
    list.sort(reverse=True)

# print(list)

largest_score = max(score_list)
largest_index = score_list.index(largest_score)
print(f'\nMost Upvoted News:',link_text_list[largest_index])
print('News Link:',link_list[largest_index])