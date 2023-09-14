import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Function to download an image
def download_image(url, folder_path, file_name):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded: {file_name}")
    else:
        print(f"Failed to download: {url}")

# Function to scrape and download images from a webpage
def scrape_and_download_images(url, folder_path):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')
        for img_tag in img_tags:
            img_url = img_tag.get('src')
            product_name = img_tag.get('alt') + '.png'
            if img_url:
                img_url = urljoin(url, img_url)
                download_image(img_url, folder_path, product_name)
    else:
        print(f"Failed to fetch webpage: {url}")

# Main function
if __name__ == "__main__":
    website_url = sys.argv[1]  # Replace with the URL of the website you want to scrape
    download_folder = website_url.split("/")[-1]  # Replace with the folder where you want to save the images

    # Create the download folder if it doesn't exist
    os.makedirs(download_folder, exist_ok=True)

    scrape_and_download_images(website_url, download_folder)

