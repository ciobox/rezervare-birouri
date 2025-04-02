from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

# Desk booking data
bookings = {}
birouri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Current date
today = datetime.date.today()

# Function to generate month view
def get_month_view():
    days_in_month = {}
    for day in range(1, 32):  # Assuming 31 days for simplicity
        try:
            day_date = datetime.date(today.year, today.month, day)
            day_name = day_date.strftime("%A")
            days_in_month[day] = {
                "date": day_date,
                "name": day_name,
                "booked": bookings.get(str(day_date), {})
            }
        except ValueError:
            break  # If the day exceeds the month's length, break out
    return days_in_month

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        ziua = request.form["ziua"]  # Acum trimitem data completă, ex: 2025-04-01
        nume = request.form["nume"]
        birou = int(request.form["birou"])

        # Inițializează ziua dacă nu există
        if ziua not in bookings:
            bookings[ziua] = {}

        # Verificare dacă biroul e deja rezervat
        if birou not in bookings[ziua].values():
            bookings[ziua][nume] = birou
        else:
            error = "Birou deja rezervat!"

    days_in_month_view = get_month_view()
    return render_template("index.html", bookings=bookings, birouri=birouri, days_in_month=days_in_month_view, error=error)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)