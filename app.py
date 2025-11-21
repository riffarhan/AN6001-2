from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/main", methods=["GET", "POST"])
def main():
    q = request.form.get("q")
    print("User name:", q)
    return render_template("main.html")

@app.route("/dbs", methods=["GET", "POST"])
def dbs():
    return render_template("dbs.html")

@app.route("/dbs_prediction", methods=["GET", "POST"])
def dbs_prediction():
    q = request.form.get("q")
    if q is None or q == "":
        return "Error: Please enter a valid number."

    q = float(q)

    model = joblib.load("dbs.pkl")

    r = model.predict([[q]])

    result = float(r[0])

    return render_template("dbs_prediction.html", prediction=result, rate=q)


if __name__ == "__main__":
    app.run(debug=True)
