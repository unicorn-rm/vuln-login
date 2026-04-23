from flask import Flask, request
import sqlite3

app = Flask(__name__)

# создаём БД при старте
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    cursor.execute("DELETE FROM users")  # чистим
    cursor.execute("INSERT INTO users VALUES ('admin', 'admin')")

    conn.commit()
    conn.close()

init_db()


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # 💀 УЯЗВИМОСТЬ
        query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{password}'"
        result = cursor.execute(query).fetchone()

        conn.close()

        if result:
            return "OK (logged in)"
        return "FAIL"

    return """
    <form method="POST">
        <input name="username" placeholder="username">
        <input name="password" placeholder="password">
        <button>login</button>
    </form>
    """

app.run(debug=True)