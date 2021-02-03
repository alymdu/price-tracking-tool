# Getting Started :sunglasses:

## Simple Price Tracking Tool for Nordstrom Rack

A simple Python script that checks the availability of an item every 15 seconds. Alerts the user when the out-of-stock product is back in stock.

**Note:** Still working on the price tracking part.

## Installation

Use `pip` to install all the necessary packages to run the getPrice.py file.

```bash
python3 -m pip install -r requirements.txt
or
pip3 install -r requirements.txt
```

## Usage

To run the script execute this command:

```bash
python3 getPrice.py links.txt
```

or you can execute this script using your Editor(don't forget about the `links.txt` file).

All the product URLs should be in the `links.txt` file.

For ex: `links.txt` file. I recommend using these links when you first try to run the script.

```text
https://www.nordstromrack.com/shop/product/2846964/reigning-champ-gym-logo-sweatshirt?color=H%20GREY%2FBLACK&size=SMALL
https://www.nordstromrack.com/s/nike-star-runner-2-sneaker/n2897218?color=001%20BLACK%2FWHITE
https://www.nordstromrack.com/shop/product/2846964/reigning-champ-gym-logo-sweatshirt?color=NAVY%2FWHITE&size=SMALL
https://www.nordstromrack.com/shop/product/2846964/reigning-champ-gym-logo-sweatshirt?color=BLACK%2FWHITE&size=SMALL
https://www.nordstromrack.com/s/n2846
```

After you run the script the output should look like this:

```bash
Status: sold out, URL: https://www.nordstromrack.com/shop/product/2846964/reigning-champ-gym-logo-sweatshirt?color=H%20GREY%2FBLACK&size=SMALL
Status: in stock, URL: https://www.nordstromrack.com/s/nike-star-runner-2-sneaker/n2897218?color=001%20BLACK%2FWHITE
Status: sold out, URL: https://www.nordstromrack.com/shop/product/2846964/reigning-champ-gym-logo-sweatshirt?color=NAVY%2FWHITE&size=SMALL
Status: sold out, URL: https://www.nordstromrack.com/shop/product/2846964/reigning-champ-gym-logo-sweatshirt?color=BLACK%2FWHITE&size=SMALL
There is something wrong with this URL https://www.nordstromrack.com/s/n2846
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)