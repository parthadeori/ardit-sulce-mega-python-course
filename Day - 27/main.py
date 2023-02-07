import requests

api_key = "246a3c2f057742c8b47478d0052a9d81"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-01-07&"\
      "sortBy=publishedAt&apiKey=246a3c2f057742c8b47478d0052a9d81"


# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])