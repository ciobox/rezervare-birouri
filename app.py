from flask import Flask, render_template, request
import datetime
return render_template("index.html", bookings=bookings, birouri=birouri, days_in_month=days_in_month_view, occupied_desks=occupied_desks)

app = Flask(__name__)

bookings = {}

birouri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

today = datetime.date.today()


def get_month_view():
    days_in_month = {}
    for day in range(1, 32):
        try:
            day_date = datetime.date(today.year, today.month, day)
            day_name = day_date.strftime("%A")
            days_in_month[day] = {
                "date": day_date,
                "name": day_name,
                "booked": bookings.get(day_name, {})
            }
        except ValueError:
            break
    return days_in_month


@app.route("/", methods=["GET", "POST"])
def index():
    error = None

    if request.method == "POST":
        ziua = request.form["ziua"]
        nume = request.form["nume"]
        birou = int(request.form["birou"])

        if birou not in bookings[ziua].values():
            bookings[ziua][nume] = birou
        else:
            error = "Birou deja rezervat!"

    occupied_desks = {}
    for ziua, rezervari in bookings.items():
        for nume, birou in rezervari.items():
            occupied_desks[birou] = nume

    days_in_month_view = get_month_view()

    return render_template(
        "index.html",
        bookings=bookings,
        birouri=birouri,
        days_in_month=days_in_month_view,
        error=error,
        occupied_desks=occupied_desks
    )

occupied_desks = []
for zi in bookings:
    for nume, birou in bookings[zi].items():
        occupied_desks.append(birou)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)