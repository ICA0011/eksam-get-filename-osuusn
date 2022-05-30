import requests
from bs4 import BeautifulSoup

url = "http://upload.itcollege.ee/~aleksei/random_files/"

def get_filename():
  file_names = []
  soup = BeautifulSoup(requests.get(url).text, 'html.parser')
  for i in soup.find_all('a'):
    file_name = f"{url}{i.get('href')}"
    file_names.append(file_name)
  return file_names[10]