"""Исправленная версия той же формы.

Закрыта ровно одна вещь — SQL-инъекция: запрос параметризован. Пароли здесь
по-прежнему лежат и сравниваются в открытом виде, это осознанная граница
стенда, а не рекомендация. Подробности в README.
"""
import sqlite3
from flask import Flask, request

app = Flask(__name__)

def check_login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # ✅ ЗАЩИТА ОТ SQL INJECTION
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))

    result = cursor.fetchone()
    conn.close()
    return result

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]

        if check_login(user, password):
            return "OK"
        return "FAIL"

    return """
    <h2>Secure Login</h2>
    <form method="POST">
        <input name="username" placeholder="username"><br>
        <input name="password" placeholder="password"><br>
        <button>login</button>
    </form>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001, debug=False)
