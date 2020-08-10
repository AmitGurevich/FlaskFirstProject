from flask import Flask, request, jsonify
app = Flask(__name__)

# A welcome message to test our server
@app.route("/")
def home():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == "__main__":
    app.run(debug=True)

