import requests

# response = requests.get("https://www.google.com")
# print(response.text)

# data = {
#     "title": "Riyan",
#     "body": "bhai",
#     "userId": 12,
# }
# headers = {"Content=type": "application/json; charset=UTF-8"}


# url = "https://jsonplaceholder.typicode.com/posts"
# response = requests.get(url)
# print(response.text)
# _________________________________________________________________


# url = "https://requests.readthedocs.io/en/latest/"
# r = requests.get(url)
# # print(r.text)

# from bs4 import BeautifulSoup

# soup = BeautifulSoup(r.text, "html.parser")
# print(soup.prettify())

# for heading in soup.find_all("h2"):
#     print(heading.text)
# ______________________________________________________________________

from bs4 import BeautifulSoup

url = "https://advice.writing.utoronto.ca/planning/paragraphs/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
paragraph = soup.find_all("p")

if (len(paragraph)) > 1:
    third_paragraph = paragraph[2]

    paragraph_text = third_paragraph.get_text()
    print(paragraph_text)

else:
    print("paragraph not found")
