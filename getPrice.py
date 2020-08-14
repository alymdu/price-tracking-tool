import urllib.request # Request library to send the requests
import itertools # I have implemented this library to iterate through the list that holds the item links
import pygame # In my opinion this is much better than receiving alerts in the text form.
import time # To make music play on computer I had to use this library. 
from bs4 import BeautifulSoup as BS # One of my favorite Python libraries. It is really great for web scraping. 

# hides the SSL Failed error
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# links for the items. In my case they are these shirts from a Canadian company called Reigning Champ.
urls = [
"https://www.nordstromrack.com/shop/product/2846964/reigning-champ-gym-logo-sweatshirt?color=H%20GREY%2FBLACK&size=SMALL",
"https://www.nordstromrack.com/shop/product/2846964/reigning-champ-gym-logo-sweatshirt?color=NAVY%2FWHITE&size=SMALL",
"https://www.nordstromrack.com/shop/product/2846964/reigning-champ-gym-logo-sweatshirt?color=BLACK%2FWHITE&size=SMALL",
"https://www.nordstromrack.com/shop/product/2846964/reigning-champ-gym-logo-sweatshirt?color=H%20CHARCOAL%2FWHITE&size=SMALL"
]

# itertools library allows to cycle the list
for link in itertools.cycle(urls):
    time.sleep(10) # it checks the current price every 10 seconds.
    usock = urllib.request.urlopen(link) # getting the page info
    data = usock.read() # reading the page info
    usock.close() 

    soup = BS(data, 'html.parser') #HTML parser

    price = soup.find('span', {'class':'pricing-and-style__sale-price'}).text # a span tag which has pricing-and-style__sale-price class associated with
    availability = soup.find('span', {'class':'cta-button__content'}).text # The items get sold out pretty quickly.

    if float(price[1:]) < 40 and availability.lower() == "add to cart": # The prices can be different. My target is to buy the item in stock and when its price is lower than $40.
        
        # if the price and availablity are both true then make the program play the alert music
        pygame.mixer.init()
        pygame.mixer.music.load("quest.ogg") #filename - some random music that I got from web.
        pygame.mixer.music.play() # This plays the music
        time.sleep(10) # For some reason my music wouldn't play. I have looked up online and saw that this sleep function solved the issue for many people. 
    
    print (price, " ", availability) # Print the price and item availability in the console.
