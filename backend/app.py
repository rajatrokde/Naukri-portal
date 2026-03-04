from flask import Flask, render_template, request, jsonify
from flask_cores import CORS
app = Flask(__name__)
CORS(app)

# Dummy user database
users = {
    "admin@gmail.com": "1234",
    "rajat@gmail.com": "devops"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"status": "error", "message": "No JSON received"}), 400

        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"status": "error", "message": "Missing credentials"}), 400

        if email in users and users[email] == password:
            return jsonify({"status": "success", "message": "Login successful"})
        else:
            return jsonify({"status": "error", "message": "Invalid credentials"}), 401

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
