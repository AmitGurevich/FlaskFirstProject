import connexion

#app = Flask(__name__)

app = connexion.App(__name__, specification_dir='./')

app.add_api('swagger.yml')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/peop")
def peop():
    return render_template("people.html")

@app.route("/anton")
def anton():
    return make_response("aaaa", 200)



if __name__ == "__main__":
    app.run(debug=True)
