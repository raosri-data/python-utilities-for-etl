from flask import Flask, jsonify
from datetime import datetime
import random

app = Flask(__name__)

@app.get("/notifications")
def notifications():
    return jsonify({
        "timestamp": datetime.utcnow().isoformat(),
        "events": [f"Event-{random.randint(1,100)}"]
    })

if __name__ == "__main__":
    app.run(debug=True)
