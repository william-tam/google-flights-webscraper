# This program scraps Google Flights and places them in the CLI. 
# The output for the CLI includes flight numbers, prices, and destinations. ie.     ---flights number-----prices------destinations-----

import requests
from bs4 import BeautifulSoup
 
# 
with open("HowTo.html") as fp: 
    soup = BeautifulSoup(fp, 'html.parser')

soup = BeautifulSoup("<html>a web page</html", 'html.parser')
print(soup)