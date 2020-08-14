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
"https://www.nordstromrack.com/shop/product/2846964/reigning-champ-gym-logo-sweatshirt?color=H%20GREY%2FBLACK&size=SMALL",
"https://www.nordstromrack.com/shop/product/2846964/reigning-champ-gym-logo-sweatshirt?color=NAVY%2FWHITE&size=SMALL",
"https://www.nordstromrack.com/shop/product/2846964/reigning-champ-gym-logo-sweatshirt?color=BLACK%2FWHITE&size=SMALL",
"https://www.nordstromrack.com/shop/product/2846964/reigning-champ-gym-logo-sweatshirt?color=H%20CHARCOAL%2FWHITE&size=SMALL"
]

# itertools library allows to cycle the list
for link in itertools.cycle(urls):
    time.sleep(10) # good practise... I guess...
    usock = urllib.request.urlopen(link)
    data = usock.read()
    usock.close()

    soup = BS(data, 'html.parser')

    price = soup.find('span', {'class':'pricing-and-style__sale-price'}).text
    availability = soup.find('span', {'class':'cta-button__content'}).text

    if float(price[1:]) < 40 and availability.lower() == "add to cart":
        
        # to play the notification music
        pygame.mixer.init()
        pygame.mixer.music.load("quest.ogg")
        pygame.mixer.music.play()
        time.sleep(10)  
    
    print (price, " ", availability)
