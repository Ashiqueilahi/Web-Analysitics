import requests
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
url = 'http://quotes.toscrape.com/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all quote elements on the page
    quotes = soup.find_all('div', class_='quote')
    
    # Create empty lists to store the extracted data
    quote_texts = []
    authors = []
    tags = []
    
    # Loop through each quote block and extract the necessary information
    for quote in quotes:
        # Extract the quote text
        text = quote.find('span', class_='text').get_text(strip=True)
        quote_texts.append(text)
        
        # Extract the author name
        author = quote.find('small', class_='author').get_text(strip=True)
        authors.append(author)
        
        # Extract the tags associated with the quote (if any)
        tag_list = quote.find_all('a', class_='tag')
        quote_tags = [tag.get_text(strip=True) for tag in tag_list]
        tags.append(', '.join(quote_tags))
    
    # Create a DataFrame to store the scraped data
    df = pd.DataFrame({
        'Quote': quote_texts,
        'Author': authors,
        'Tags': tags
    })
    
    # Display the extracted data
    print(df)
    
    # Optionally save the data to a CSV file
    df.to_csv('quotes.csv', index=False)

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")