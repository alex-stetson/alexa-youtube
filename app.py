from flask import Flask, request, jsonify
from lambda_function import lambda_handler

app = Flask(__name__)

@app.route('/', methods=["POST"])
def handle_request():
    data = request.get_json(force=True)
    result = lambda_handler(data, None)
    resp = jsonify(result)
    resp.status_code = 200
    return resp

if __name__ == "__main__":
    app.run()