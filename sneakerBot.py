from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import requests

myURL = 'https://www.nike.com/launch/'

html_file = uReq(myURL)

page = html_file.read()

html_file.close()

parsed_html=soup(page, "html.parser")

containers = parsed_html.findAll("div", {"class":"figcaption-content"})
erai = parsed_html.findAll("h3", {"class":"ncss-brand u-uppercase text-color-grey mb-1-sm mb0-md mb-3-lg fs12-sm fs14-md"})
buttons = parsed_html.findAll("button", {"class":"cta-btn u-uppercase cta-btn ncss-btn text-color-white ncss-brand d-sm-b d-lg-ib pr5-sm pl5-sm pt3-sm pb3-sm d-sm-ib bg-black test-buyable buyable-full-width buyable-feed"})

e = str(len(erai))
b = str(len(buttons))
s = str(len(containers))

print("Shoes found: " + s)
print("Parsing...")
# print("Test: " + e)
# print("Buyable: " + b)

shoeOne = containers[0]

shoeName = shoeOne.div.h3
print(shoeName)

print("Finding shoe name from config file...")
n = open('config.txt', 'r')
n_content = n.read()
print(n_content)
n.close()
