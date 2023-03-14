from flask import Flask, render_template, request
import marks as m

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def marks():
    print("tututut")
    if request.method == "POST":
        print("dasdsa")
        hrs = request.form["hrs"]
        marks_pred = m.marks_prediction(float(hrs))
        mk = marks_pred
        return render_template("index.html", my_marks=mk)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)