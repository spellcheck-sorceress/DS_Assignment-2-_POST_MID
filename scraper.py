import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "http://books.toscrape.com/catalogue/"
url = "http://books.toscrape.com/catalogue/page-1.html"

books = []

while url:
    print(f"Scraping: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for book in soup.find_all("article", class_="product_pod"):
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        rating = book.p["class"][1]  # e.g. "Three"
        
        books.append({
            "Title": title,
            "Price": price,
            "Rating": rating
        })

    # Go to next page if it exists
    next_btn = soup.find("li", class_="next")
    url = BASE_URL + next_btn.a["href"] if next_btn else None

    time.sleep(1)  # be polite to the server!

df = pd.DataFrame(books)
df.to_csv("data.csv", index=False)
print(f"Done! {len(books)} books scraped.")