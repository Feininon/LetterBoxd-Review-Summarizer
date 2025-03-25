import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        reviews = soup.find_all('p')
        page_data = "\n".join([review.get_text() for review in reviews])  # Collect all reviews as text
        return page_data
    else:
        print(f"Failed to retrieve page {url}")
        return None

def scrape_multiple_pages(base_url, total_pages):
    with open(f"{formatted_name}_reviews.txt", 'a', encoding="utf-8") as file:  # Open the file in append mode
        for page_num in range(1, total_pages + 1):
            url = f"{base_url}/page/{page_num}"
            print(f"Scraping {url}")
            page_data = str(scrape_page(url))
            # If data is successfully scraped, write to the file
            if page_data:
                file.write(f"Page {page_num}:\n")
                file.write(page_data)
                file.write("\n" + "-"*40 + "\n")  # Separate each page with a line of dashes
            else:
                print(f"No data found on {url}")
                
# Usage example:
movie_name = input("Enter the name of the movie you want to summarize: ")
formatted_name = movie_name.lower().replace(" ", "-")
base_url = f"https://letterboxd.com/film/{formatted_name}/reviews"
total_pages = 12 # or set this to the number of pages you need to scrape

scrape_multiple_pages(base_url, total_pages)

                