from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Matrix Multiplier API"

@app.route('/multiply', methods=["POST"])
def multiply():
    data = request.get_json()
    matrixA = data.get("matrixA")
    matrixB = data.get("matrixB")

    try:
        result = np.dot(matrixA, matrixB)
        return jsonify({"result": result.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Make sure this part is present!
if __name__ == "__main__":
    app.run(debug=True)
