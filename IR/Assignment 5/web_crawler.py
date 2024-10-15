import requests
from bs4 import BeautifulSoup
import yake

array = []
def get_text(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  text_content = soup.find_all('p')
  text = ' '.join([para.get_text() for para in text_content])
  text = text.lower()
  return text

def extract(url):
  text = get_text(url)
  kw_extractor = yake.KeywordExtractor(lan="en", n=1, top=100)
  keywords = kw_extractor.extract_keywords(text)
  for kw, score in keywords:
      array.append(kw)
def display():
  print("Length: ", len(array))
  for kw in array:
    print(kw, ", ")

extract('https://en.wikipedia.org/wiki/Education')
display()
