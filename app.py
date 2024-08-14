from flask import Flask, request, jsonify
from validate_json import validate_json

app = Flask(__name__)

data_content = {"key_1": "value_1", "key_2": "value_2"}


@app.route("/")
def index():
    return {"message": "Welcome to the templates app server!"}


@app.route("/validate_json", methods=["POST"])
def validate_data():
    data = request.json
    max_depth = request.args.get('max_depth', default=2, type=int)

    if not isinstance(data, dict):
        return jsonify({"valid": False, "error": "Provided data is not a valid JSON object"}), 400

    is_valid = validate_json(data, max_depth)

    return jsonify({"valid": is_valid}), 200


@app.route("/data", methods=["GET"])
def get_data():
    return data_content


@app.route("/data/<key>", methods=["GET"])
def get_data_per_key(key: str):
    if key in data_content:
        return {key: data_content[key]}
    return {"message": f"The requested parameter {key} was not found"}


@app.route("/data/delete/<key>", methods=["DELETE"])
def delete_data(key: str):
    if key in data_content:
        del data_content[key]
        return {"message": f"Parameter {key} and its content was deleted successfully"}
    else:
        return {"message": f"The parameter {key} was not found"}


@app.route('/update-data', methods=['PUT'])
def update_data():
    new_data = request.json

    if not isinstance(new_data, dict):
        return jsonify({"error": "Invalid data format"}), 400

    data_content.update(new_data)

    return jsonify({'data_content': data_content}), 200


@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
