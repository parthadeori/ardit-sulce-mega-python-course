import requests
from send_email import send_email

api_key = "246a3c2f057742c8b47478d0052a9d81"

### NEED TO UPDATE THIS URL FROM NEWSAPI IF YOU RUNNING THIS SCRIPT ON OR AFTER 08-01-2023 
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-01-07&sortBy=publishedAt&apiKey=246a3c2f057742c8b47478d0052a9d81"


# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content['articles']:
    if article['description'] is not None:
        body = body + article['title'] + "\n" + article['description'] + 2*"\n"

body = body.encode('utf-8')
send_email(message=body)