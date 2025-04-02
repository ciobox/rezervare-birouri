from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Initial desks data
desks = {
    f"desk{i}": {"reserved": False, "name": "", "date": ""} for i in range(1, 11)
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/desks')
def get_desks():
    return jsonify(desks)

@app.route('/api/book', methods=['POST'])
def book_desk():
    data = request.json
    desk_id = data.get('desk')
    name = data.get('name')
    date = data.get('date')

    if desk_id in desks:
        desks[desk_id] = {
            "reserved": True,
            "name": name,
            "date": date
        }
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "Desk not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)