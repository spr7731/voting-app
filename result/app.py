from flask import Flask
import redis, os

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
r = redis.Redis(host=REDIS_HOST, port=6379, db=0, decode_responses=True)

app = Flask(__name__)

@app.route("/")
def index():
    a = r.get("A") or "0"
    b = r.get("B") or "0"
    return f"<h1>Results</h1><p>A = {a} <br> B = {b}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
