import requests
from bs4 import BeautifulSoup

# Define the URL you want to scrape
url = 'https://facebook.com'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data from the page
# For example, let's extract all the links on the page
links = soup.find_all('a')

# Print the links
for link in links:
    print(link.get('href'))
