from flask import Flask, render_template

app = Flask(__name__),connexion.App(__name__, specification_dir='./')

app.add_api('swagger.yml')

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/peop')
def people():
    
    return render_template('people.html')

if __name__ == "__main__":
    app.run(debug=True)

