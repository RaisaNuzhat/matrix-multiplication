from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        try:
            matrixA = eval(request.form["matrixA"])
            matrixB = eval(request.form["matrixB"])
            result = np.matmul(matrixA, matrixB).tolist()
        except Exception as e:
            error = "Invalid input or incompatible matrices!"
    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
