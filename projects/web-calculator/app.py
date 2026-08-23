"""Web Calculator — a Flask frontend wired up for you, calculation logic left for you to fill in.

Run it with:
    pip install flask
    python app.py
Then open http://127.0.0.1:5000 in your browser.
"""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        operation = request.form.get("operation")

        if not num1 or not num2 or not operation:
            error = "Please fill in both numbers and choose an operation."
        else:
            result = calculate(float(num1), float(num2), operation)
            if isinstance(result, str):
                error = result
                result = None

    return render_template("index.html", result=result, error=error)


def calculate(num1, num2, operation):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Can't divide on zero"

    return result


if __name__ == "__main__":
    app.run(debug=True)
