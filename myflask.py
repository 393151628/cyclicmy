from flask import Flask, request, jsonify
import cyclicmy

app = Flask(__name__)


@app.route("/api/compute", methods=['POST'])
def recive_code():
    data = request.get_json()
    num = cyclicmy.compute(data['code'])
    return jsonify({"cyclic": num})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
