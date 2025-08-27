from flask import Flask, render_template, request, redirect
import sqlite3
import datetime

app = Flask(__name__)

# DB init
def init_db():
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS expenses
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL,
                    category TEXT,
                    description TEXT,
                    date TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses")
    rows = cur.fetchall()
    conn.close()

    # Summary for charts
    categories = {}
    for row in rows:
        categories[row[2]] = categories.get(row[2], 0) + row[1]

    dates = {}
    for row in rows:
        dates[row[4]] = dates.get(row[4], 0) + row[1]

    return render_template("index.html", expenses=rows, categories=categories, dates=dates)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        amount = float(request.form["amount"])
        category = request.form["category"]
        description = request.form["description"]
        date = request.form["date"]

        conn = sqlite3.connect("expenses.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
                    (amount, category, description, date))
        conn.commit()
        conn.close()
        return redirect("/")
    return render_template("add.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
