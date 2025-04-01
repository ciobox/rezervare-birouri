from flask import Flask, render_template, request

app = Flask(__name__)

# Data saved temporarily
bookings = {
    "Luni": {},
    "Marti": {},
    "Miercuri": {},
    "Joi": {},
    "Vineri": {}
}
birouri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ziua = request.form["ziua"]
        nume = request.form["nume"]
        birou = int(request.form["birou"])

        if birou not in bookings[ziua].values():
            bookings[ziua][nume] = birou

    return render_template("index.html", bookings=bookings, birouri=birouri)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)