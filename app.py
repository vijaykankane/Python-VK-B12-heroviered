from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route('/get-config', methods=['GET'])
def get_config():
    try:
        if not os.path.exists('config_data.json'):
            return jsonify({"error": "Configuration data not found."}), 404

        with open('config_data.json') as json_file:
            config_data = json.load(json_file)

        return jsonify(config_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
