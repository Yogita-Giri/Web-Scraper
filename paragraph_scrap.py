import requests
from bs4 import BeautifulSoup

def scrape_javatpoint():
    url = "https://www.javatpoint.com/"
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract information based on the HTML structure of the website
        # Replace this part with the actual elements you want to scrape
        title = soup.title.text.strip()
        paragraphs = [p.text.strip() for p in soup.find_all('p')]
        
        # Print the extracted information
        print(f"Title: {title}\n")
        print("Paragraphs:")
        for i, paragraph in enumerate(paragraphs, start=1):
            print(f"{i}. {paragraph}")
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")

if __name__ == "__main__":
    scrape_javatpoint()
