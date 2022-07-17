import json
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/smartphones', methods=['GET'])
def search():
    sorted_data = []
    price = request.args.get('price', type=int)
    f = open('satukzParser/smartphones.json', 'r')
    datas = json.load(f)
    for data in datas:
        if data['price']:
            if price == int(data['price']):
                sorted_data.append(data)
    return jsonify(sorted_data)


if __name__ == '__main__':
    app.run(debug=True)
