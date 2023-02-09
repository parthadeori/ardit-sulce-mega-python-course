from flask import Flask, render_template

app = Flask("Website")

@app.route("/")

def home():
    return render_template(r"Day - 29\template\index.html")


app.run(debug=True)