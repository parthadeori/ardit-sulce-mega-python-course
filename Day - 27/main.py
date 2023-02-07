import requests

api_key = "246a3c2f057742c8b47478d0052a9d81"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-01-07&"\
      "sortBy=publishedAt&apiKey=246a3c2f057742c8b47478d0052a9d81"

request = requests.get(url)
content = request.text

print(content)