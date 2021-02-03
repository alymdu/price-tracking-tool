"""
@alymbektech
"""

"""
urllib.request - package to send out requests
itertools - library to iterate through the list that holds the item URLs
pygame - library to play a sound
time - library to pause the script when needed
bs4 - library to read HTML elements
"""
import urllib.request
import itertools
import pygame
import time
import sys
import re
from bs4 import BeautifulSoup as BS

# hides the SSL Failed error
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# get the links in the txt file
def openLinks(filename):
    links = []
    with open(filename) as f:
        for line in f:
            line = re.sub('\,|\"|\'', '', line)
            links.append(line.strip())
    return links

def checkStock(links):
    
    for link in itertools.cycle(links):
        try:
            usock = urllib.request.urlopen(link) # getting the page info
            data = usock.read() # reading the page
            usock.close() 
            soup = BS(data, 'html.parser') #HTML parser
            availability = soup.find('span', {'class':'cta-button__content'}).text.lower()
            if availability == "add to cart":
                availability = "in stock"
                pygame.mixer.init()
                pygame.mixer.music.load("quest.ogg") #filename - some random music that I got from internet.
                pygame.mixer.music.play() # this line plays that
                time.sleep(10) # for some reason the music won't start playing if you don't set a sleep. 
            print (f'Status: {availability}, URL: {link}') # Print the price and item availability in the console.
            time.sleep(15) # 15 sec pause
        except:
            print (f'There is something wrong with this URL {link}') # Print the price and item availability in the console.
            time.sleep(15)
    return 

def main():
    links = openLinks(sys.argv[1])
    checkStock(links)

if __name__ == '__main__':
    main()