from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/customer-groups', methods=['GET'])
def get_customer_groups():
    store_hash = "k6jflwesl8"
    access_token = "25ouk455kn9lnxix6huouyb0zurhbm9"

    url = f"https://api.bigcommerce.com/stores/{store_hash}/v2/customer_groups"
    headers = {
        "X-Auth-Token": access_token,
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": response.text}), response.status_code

@app.route('/')
def health_check():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run()
