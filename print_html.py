import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to print the parsed HTML of a webpage
def print_parsed_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())
    else:
        print(f"Failed to fetch webpage: {url}")

# Main function
if __name__ == "__main__":
    website_url = sys.argv[1]  # Replace with the URL of the website you want to scrape

    print_parsed_html(website_url)

