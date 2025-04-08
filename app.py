from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "running"})

@app.route('/customer-groups')
def get_customer_groups():
store_hash = os.getenv("STORE_HASH", "k6jflwesl8")
access_token = os.getenv("ACCESS_TOKEN", "25ouk455kn9lnxix6huouyb0zurhbm9")

    url = f"https://api.bigcommerce.com/stores/{store_hash}/v2/customer_groups"
    headers = {
        "X-Auth-Token": access_token,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return jsonify(response.json())
        return jsonify({"error": response.text}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500
