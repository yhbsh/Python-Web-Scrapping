import sys
import requests
from bs4 import BeautifulSoup

# Function to save the parsed HTML of a webpage to a file
def save_parsed_html(url, output_file):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(soup.prettify())
        print(f"Parsed HTML saved to {output_file}")
    else:
        print(f"Failed to fetch webpage: {url}")

# Main function
if __name__ == "__main__":
    website_url = sys.argv[1]  # Replace with the URL of the website you want to scrape
    output_file = "out.html"  # Name of the output file

    save_parsed_html(website_url, output_file)

