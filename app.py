from flask import Flask, render_template,make_response

import connexion

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/anton")
def anton():
    return make_response("aaaa", 200)

if __name__ == "__main__":
    app.run(debug=True)
