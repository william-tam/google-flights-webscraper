# This program scraps Google Flights and places them in the CLI. 
# The output for the CLI includes flight numbers, prices, and destinations. ie.     ---flights number-----prices------destinations-----

from http.server import executable
import requests
# the main component that interacts with webpages
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# PATH has been automated by chromDriverManager service.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Google flights url, from sj to denver.
url = 'https://www.google.com/travel/flights/search?tfs=CBwQAhooagwIAhIIL20vMGYwNHYSCjIwMjItMDEtMjhyDAgDEggvbS8wMmNsMRooagwIAxIIL20vMDJjbDESCjIwMjItMDItMDFyDAgCEggvbS8wZjA0dnABggELCP___________wFAAUgBmAEB'

# Prevent the DevTools solution message from popping up by using Options functionality.
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


# Open the chrome url page.
# driver = webdriver.Chrome(executable_path=url, options=options)
driver.get(url)
