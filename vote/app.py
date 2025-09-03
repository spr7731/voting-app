from flask import Flask, request, redirect, render_template_string
import redis, os

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=REDIS_HOST, port=6379, db=0, decode_responses=True)

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<title>Vote</title>
<h1>Voting Booth</h1>
<form action="/vote" method="post">
  <button name="option" value="A">Vote A</button>
  <button name="option" value="B">Vote B</button>
</form>
<p>Current: A = {{a}}, B = {{b}}</p>
"""

@app.route("/", methods=["GET"])
def index():
    a = r.get("A") or "0"
    b = r.get("B") or "0"
    return render_template_string(TEMPLATE, a=a, b=b)

@app.route("/vote", methods=["POST"])
def vote():
    option = request.form.get("option")
    if option in ("A", "B"):
        r.incr(option)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
