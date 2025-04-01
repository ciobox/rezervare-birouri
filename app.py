from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

# Desk booking data
bookings = {
    "Luni": {1: "Radu Ciobotaru - Birou 4", 2: "Maria Prodan - Birou 1", 3: "Cosmin Miscu - Birou 6"},
    "Marti": {},
    "Miercuri": {},
    "Joi": {},
    "Vineri": {1: "Cosmin Miscu - Birou 1"}
}

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
            days_in_month[day] = {"date": day_date, "name": day_name, "booked": bookings.get(day_name, {})}
        except ValueError:
            break  # If the day exceeds the month's length, break out
    return days_in_month


@app.route("/", methods=["GET", "POST"])
def index():
    birouri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    if request.method == "POST":
        ziua = request.form["ziua"]
        nume = request.form["nume"]
        birou = int(request.form["birou"])
        
        if birou not in bookings[ziua].values():
            bookings[ziua][nume] = birou
    
    return render_template("index.html", bookings=bookings, birouri=birouri)
    days_in_month = get_month_view()
    return render_template("index.html", days_in_month=days_in_month)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)