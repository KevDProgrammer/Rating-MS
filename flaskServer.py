import time
from flask import Flask, render_template, request
from flask import send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("RatingTester.html")

@app.route("/nr-page")
def nr():
    return render_template("nr.html")

@app.route("/na-page")
def na():
    return render_template("na.html")

@app.route("/nr2-page")
def nr2():
    return render_template("nr2.html")

@app.route("/rating-page")
def sorted_rating():
    return render_template("SortedRating.html")

@app.route("/bridge.js")
def bridge_js():
    return send_from_directory("templates", "bridge.js")

@app.route("/rating", methods=["POST"])
def rating_manager():
    data = request.get_json()
    action = data["action"]
    title = data["title"]

    with open("request.txt", "w") as f:
        f.write(f"action={action}\n")
        f.write(f"title={title}")

    # the display then holds the result within response for the ratings
    time.sleep(0.2)
    with open("response.txt", "r") as f:
        rating_response = f.read()
    return rating_response

if __name__ == "__main__":
    app.run(debug=True)