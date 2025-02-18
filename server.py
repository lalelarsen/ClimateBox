from flask import Flask, request, jsonify
from gsheet_connector import send_data

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def handle_post():
    data = request.get_json()  # Expecting JSON payload
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    # Example: extract a 'name' field from the JSON payload
    # temperature = data.get('temperature')
    # humidity = data.get('humidity')
    print(data)

    # Do something with the data...
    response = {
        "message": "success!"
    }

    send_data(data)

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)