import json
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/smartphones', methods=['GET'])
def search():
    price = request.args.get('price', type=int)
    f = open('satukzParser/smartphones.json', 'r')
    datas = json.load(f)
    for data in datas:
        if data['price']:
            if price == int(data['price']):
                return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
