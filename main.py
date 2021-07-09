import requests as request
from bs4 import BeautifulSoup as bs

github_user = input('Input GitHub User: ')
url = 'https://github.com/' + github_user
r = request.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_image)