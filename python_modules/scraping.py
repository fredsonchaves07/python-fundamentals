import requests
from bs4 import BeautifulSoup

url = "https://pt.stackoverflow.com/questions/tagged/python"
response = requests.get(url)
html = BeautifulSoup(response.text, "html.parser")

for question in html.select(".question-summary"):
    title = question.select_one(".question-hyperlink").text
    date = question.select_one(".relativetime").text
    vote_count = question.select_one(".vote-count-post").text

    print(title)
