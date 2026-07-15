from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        amount REAL,
        category TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()

    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO expenses(title,amount,category) VALUES(?,?,?)",
        (data["title"], data["amount"], data["category"])
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Expense Added"})

@app.route("/expenses")
def expenses():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    data = c.execute("SELECT * FROM expenses").fetchall()
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)