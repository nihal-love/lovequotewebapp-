from flask import Flask, render_template, request, redirect, url_for
import random, os

app = Flask(__name__)
app.secret_key = "shahu_secret"

file_name = "quotes.txt"

if os.path.exists(file_name):
    with open(file_name,"r",encoding="utf-8") as f:
        quotes = f.read().splitlines()
else:
    quotes = [
        "I love you more than yesterday ❤️",
        "You are my peace in this noisy world 💫",
        "Shahu makes my heart skip a beat 💓",
        "Every moment with you is magic ✨",
        "You are my sunshine ☀️"
    ]

emojis = ["💖","😍","💕","😘","💫"]

@app.route("/", methods=["GET","POST"])
def login():

    if request.method=="POST":

        password = request.form.get("password")

        if password == "shahu58":
            return redirect(url_for("home"))

    return render_template("login.html")

@app.route("/home", methods=["GET","POST"])
def home():

    message=""
    quote=random.choice(quotes)+" "+random.choice(emojis)

    if request.method=="POST":

        new_quote=request.form.get("new_quote")

        if new_quote:

            quotes.append(new_quote)

            with open(file_name,"a",encoding="utf-8") as f:
                f.write(new_quote+"\n")

            message="Quote saved forever 💖"

    return render_template("index.html",quote=quote,message=message)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)