import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

def scrape_products(url):
    """Scrape product details from the provided URL."""
    # Make a request to get the content of the website
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all products using the class name
    products = soup.find_all('div', class_='product-box')

    product_list = []

    for product in products:
        # Extracting title
        title_element = product.find('h3', class_='product-title')
        title = title_element.text.strip() if title_element else ""

        # Extracting image source
        image_element = product.find('img', class_='lazyload')
        image_src = image_element['data-src'] if image_element else ""

        # Extracting price
        price_element = product.find('span', class_='product-price')
        price = price_element.text.strip() if price_element else ""

        # Vendor name
        vendor_name = url.split('/')[-1]

        product_data = {
            'Title': title,
            'Image Src': image_src,
            'Price / International': price,
            'Vendor': vendor_name
        }

        product_list.append(product_data)

    return product_list

def save_to_excel(product_list, filename='products.xlsx'):
    """Save the scraped product details to an Excel file."""
    df = pd.DataFrame(product_list)
    df.to_excel(filename, index=False)

def save_to_csv(product_list, filename='products.csv'):
    """Save the scraped product details to a CSV file."""
    df = pd.DataFrame(product_list)
    df.to_csv(filename, index=False)


def main():
    """Main function to handle the script execution."""
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <website_url>")
        sys.exit(1)
    
    url = sys.argv[1]
    product_list = scrape_products(url)
    # save_to_excel(product_list)
    save_to_csv(product_list)
    print(f"Products saved to products.csv")

if __name__ == "__main__":
    main()

