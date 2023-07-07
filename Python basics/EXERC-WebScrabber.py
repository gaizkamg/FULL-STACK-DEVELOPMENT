from bs4 import BeautifulSoup
import inflection
import requests
import nltk

url_page = 'https://www.dailysmarty.com/topics/python'
response = requests.get(url_page)


elements = BeautifulSoup(response.content, 'html.parser')
h2 = elements.find_all('h2')

for headers in h2:
    links = headers.find_all('a')
    for link in links:
        link_url = link['href'][7:]
        link_url = link_url.replace('-', ' ')
        tokens = nltk.word_tokenize(link_url)
        tagged = nltk.pos_tag(tokens)

        prepositions = [word for word, pos in tagged if pos == 'IN']
        # print(prepositions)
        link_url = inflection.titleize(link_url, exceptions=prepositions)
        print(f'"{link_url}"')
