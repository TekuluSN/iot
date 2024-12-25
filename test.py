from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json  # Get JSON data from the client
    print(f"Received data: {data}")
    return jsonify({"status": "success", "message": "Data received successfully!"})

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello from Flask server!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Run on all interfaces
