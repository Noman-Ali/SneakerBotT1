from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import requests

myURL = 'https://www.nike.com/launch/'

html_file = uReq(myURL)

page = html_file.read()

html_file.close()

parsed_html=soup(page, "html.parser")

#print(parsed_html)
