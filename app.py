"""СТЕНД. Форма входа с намеренной SQL-инъекцией.

Уязвимость в строке с f-string ниже оставлена сознательно — она и есть
предмет стенда. Приложение поднимается только на петле и без отладки:
в интернет его выставлять нельзя.
"""
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

if __name__ == "__main__":
    # только петля и без debug: отладочный режим Flask даёт консоль
    # Werkzeug, то есть выполнение кода — это уже не учебная дыра
    app.run(host="127.0.0.1", port=5000, debug=False)
