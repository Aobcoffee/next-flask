from flask import Flask, jsonify
from flask_cors import CORS

# app instance
app = Flask(__name__)
CORS(app)

@app.route("/api/home")
def return_home():
    return jsonify({
        'message': 'This is the home page!'
    })


if __name__ == '__main__':
    app.run(debug=True, port=8080)