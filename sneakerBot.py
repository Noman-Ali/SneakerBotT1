from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import requests

myURL = 'https://www.nike.com/launch/'

html_file = uReq(myURL)

page = html_file.read()

html_file.close()

parsed_html=soup(page, "html.parser")

containers = parsed_html.findAll("div", {"class":"ncss-col-sm-12 full"})

print(len(containers))
