from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]

        # уязвимость
        if user == "admin" and password == "admin":
            return "OK"
        return "FAIL"

    return """
    <form method="POST">
        <input name="username">
        <input name="password">
        <button>login</button>
    </form>
    """

app.run()