from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

# Desk booking data (this should be dynamic, possibly from a database)
bookings = {
    "Luni": {"Radu Ciobotaru - Birou 4": 1, "Maria Prodan - Birou 1": 2, "Cosmin Miscu - Birou 6": 3},
    "Marti": {},
    "Miercuri": {},
    "Joi": {},
    "Vineri": {"Cosmin Miscu - Birou 1": 1}
}

birouri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Current date
today = datetime.date.today()

# Function to generate month view
def get_month_view():
    # Create a dictionary of days with dates and availability for desks
    days_in_month = {}
    for day in range(1, 32):  # Assuming 31 days for simplicity
        try:
            day_date = datetime.date(today.year, today.month, day)
            day_name = day_date.strftime("%A")
            days_in_month[day] = {
                "date": day_date,
                "name": day_name,
                "booked": bookings.get(day_name, {})
            }
        except ValueError:
            break  # If the day exceeds the month's length, break out
    return days_in_month

@app.route("/", methods=["GET", "POST"])
def index():
    birouri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    error = None

    if request.method == "POST":
        ziua = request.form["ziua"]
        nume = request.form["nume"]
        birou = int(request.form["birou"])

        if birou in bookings[ziua].values():
            error = "Birou deja rezervat!"
        else:
            bookings[ziua][nume] = birou

    days_in_month_view = get_month_view()
    return render_template("index.html", bookings=bookings, birouri=birouri, days_in_month=days_in_month_view, error=error)
    # Get the month view
    days_in_month_view = get_month_view()
    return render_template("index.html", bookings=bookings, birouri=birouri, days_in_month=days_in_month_view)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)