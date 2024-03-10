import requests
from bs4 import BeautifulSoup


# URL of the webpage to scrape
url = "https://www.gamedev.net/news/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the news articles
    news_articles = soup.find_all("div", class_="media-body")
    print(news_articles)

    # Extract and print the titles and links of the articles
    for article in news_articles:
        title = article.find("h3").text.strip()
        link = article.find("a")["href"]
        print(title)
        print("Link:", link)
        print()
else:
    print("Failed to retrieve the webpage.")
