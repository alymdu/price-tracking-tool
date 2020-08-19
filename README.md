# Getting Started :sunglasses:

## Simple Price Tracking Tool for Nordstrom Rack

A simple Python script that checks the price of an item every 10 seconds. Alerts the user if the price value is below a certain amount.

## Installation

Use the package manager [pip] and install all the libraries in getPrice.py file.

```python
import urllib.request
import itertools
import pygame
import time
from bs4 import BeautifulSoup as BS
```

## Usage

This script is really easy to use. All you have to do is just change the links and tags and you should be able to start price tracking.

I am tracking prices of 4 different items:

```python
urls = [ 
"https://www.nordstromrack.com/shop/product/2846964/reigning-champ-gym-logo-sweatshirt?color=H%20GREY%2FBLACK&size=SMALL",
"https://www.nordstromrack.com/shop/product/2846964/reigning-champ-gym-logo-sweatshirt?color=NAVY%2FWHITE&size=SMALL",
"https://www.nordstromrack.com/shop/product/2846964/reigning-champ-gym-logo-sweatshirt?color=BLACK%2FWHITE&size=SMALL",
"https://www.nordstromrack.com/shop/product/2846964/reigning-champ-gym-logo-sweatshirt?color=H%20CHARCOAL%2FWHITE&size=SMALL"
]
```

To run the script simply type `python getPrice.py`

And the output should look like this:

```python
 $59.98   Add to Cart
 $79.97   Sold Out
 $79.97   Add to Cart
 $59.98   Add to Cart
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)