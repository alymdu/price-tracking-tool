import urllib.request
import itertools
import pygame
import time
from bs4 import BeautifulSoup as BS

# hides the SSL Failed error
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# links for the items. In my case they are from NordstromRack 
urls = [
"https://goldenarchesunlimited.com/products/mcdonalds-x-funko-pop-ad-icons-limited-edition-5pk"
]

# itertools library allows to cycle the list
for link in itertools.cycle(urls):
    time.sleep(10) # good practise... I guess...
    
    try:
        usock = urllib.request.urlopen(link)
        pygame.mixer.init()
        pygame.mixer.music.load("quest.ogg")
        pygame.mixer.music.play()
        time.sleep(10)  
    except urllib.error.HTTPError:
        print ("Damn")
    
    

    """

    if float(price[1:]) < 40 and availability.lower() == "add to cart":
        
        # to play the notification music
        pygame.mixer.init()
        pygame.mixer.music.load("quest.ogg")
        pygame.mixer.music.play()
        time.sleep(10)  
    """

#    print (price)
