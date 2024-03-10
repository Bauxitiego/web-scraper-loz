import requests
from bs4 import BeautifulSoup
import csv

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

    # Open a CSV file in write mode
    with open("news.csv", "w", newline="", encoding="utf-8") as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)

        # Write the header row
        csv_writer.writerow(["Title", "Link"])

        # Extract and write the titles and links of the articles to the CSV file
        for article in news_articles:
            title = article.find("h3").text.strip()
            link = article.find("a")["href"]
            csv_writer.writerow([title, link])
            print(f"Title: {title}\nLink: {link}\n")
    print("Data saved to news.csv")
else:
    print("Failed to retrieve the webpage.")
