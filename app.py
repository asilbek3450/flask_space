from flask import Flask, render_template, request, redirect, url_for, session, make_response
from datetime import datetime

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/set_language/<lang>")
def set_language(lang):
    # tilni session’da saqlaymiz
    session["lang"] = lang
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    last_visit = request.cookies.get("last_visit")
    lang = session.get("lang", "uz")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "student" and password == "12345":
            return f"Xush kelibsiz, {username}!"
        else:
            return "Login yoki parol xato!"

    resp = make_response(render_template("login.html", lang=lang, last_visit=last_visit))
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    resp.set_cookie("last_visit", now, max_age=60*60*24*7)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
