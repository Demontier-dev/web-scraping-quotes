import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Coleta todas as citações (frase + autor)
quotes = soup.find_all("div", class_="quote")

rows = []

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    rows.append([text, author])

# Salva os dados em CSV
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Frase", "Autor"])
    writer.writerows(rows)

print("quotes.csv created successfully")