from bs4 import BeautifulSoup
import requests
import pandas as pd

# Add header and  url
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
url = "https://en.wikipedia.org/wiki/List_of_national_capitals"
#url = "https://www.amazon.com/"
r = requests.get(url)

# Initiate beautiful and list element to extract all the rows in the table
soup = BeautifulSoup(r.content, "html.parser")
#print(soup.find_all('table'))
#print(soup.prettify())
table = soup.find_all('table')[0] # Grab the first table
print(table)
