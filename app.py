from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Simple in-memory reservation storage
desks = {
    "desk1": False,
    "desk2": False,
    "desk3": False,
    "desk4": False,
    "desk5": False,
    "desk6": False,
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/desks')
def get_desks():
    return jsonify(desks)

@app.route('/api/book/<desk_id>', methods=['POST'])
def book_desk(desk_id):
    if desk_id in desks:
        desks[desk_id] = not desks[desk_id]  # Toggle
        return jsonify({"status": "success", "reserved": desks[desk_id]})
    return jsonify({"status": "error", "message": "Desk not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)