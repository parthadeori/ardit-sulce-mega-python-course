import requests
from send_email import send_email

api_key = "246a3c2f057742c8b47478d0052a9d81"

topic = "tesla"

### YOU HAVE TO UPDATE THIS URL FROM NEWSAPI IF YOU ARE RUNNING THIS SCRIPT ON OR AFTER MARCH, 2023
url = f"https://newsapi.org/v2/everything?q={topic}&from=2023-01-08&sortBy=publishedAt&apiKey=246a3c2f057742c8b47478d0052a9d81&language=en"


# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content['articles'][:20]:
    if article['description'] is not None:
        body = "Subject: Today's News" \
+ "\n" + body + article['title'] + "\n" + article['description'] + "\n" + article["url"] + 2*"\n"

body = body.encode('utf-8')
send_email(message=body)