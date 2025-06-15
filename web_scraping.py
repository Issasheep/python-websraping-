import requests
from bs4 import BeautifulSoup
website_url = "https://meta.wikimedia.org/wiki/List_of_Wikipedias/Table"

r = requests.get(website_url)
#response = requests.get("https://realpython.com/python-requests")

#print (response)

# check status code for response received
# success code - 200

# Parsing the HTML
name = website_url.split(".")[-2]


soup = BeautifulSoup(r.content, 'html.parser')

#f = open(f"{name}.txt", "x")
f = open(f"{name}.txt", "w")
f.write (soup.prettify())

f.read()")
f.close()





