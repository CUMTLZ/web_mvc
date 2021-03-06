
import json
from flask import Flask, request, jsonify
JSON_AS_ASCII = False
app = Flask(__name__)


FILE = './test.json'
def get_database():
    with open(FILE, 'r') as file:
        database = json.loads(file.read())
    return database

def set_database(database):
    print(database)
    with open(FILE, 'w') as file:
        file.write(json.dumps(database))


@app.route('/', methods=['GET'])
def index():
    return 'hello world', 200


@app.route('/api/tasks/', methods=['GET'])
def query_all():
    data = get_database()
    return jsonify(data), 200


@app.route('/api/tasks/', methods=['POST'])
def insert():
    new_data = str(request.get_data(), encoding='utf-8')
    try:
        new_data = json.loads(new_data)
    except:
        return '请检查数据合法性', 403

    database = get_database()
    for item in database:
        if new_data['id'] == item['id']:
            return '创建失败，已存在id=%s' % new_data['id'], 403

    database.append(new_data)
    set_database(database)
    return jsonify(database), 200


@app.route('/api/tasks/<id>', methods=['GET'])
def query_by_id(id=None):
    # 返回一个指定ID的Todo任务
    try:
        id = int(id)
    except:
        return 'id必须是int类型', 403

    database = get_database()
    for item in database:
        if id == item['id']:
            return jsonify(item), 200
    return '查找失败，不存在id=%s的项' % (id), 404


@app.route('/api/tasks/<id>', methods=['DELETE'])
def delete_by_id(id=None):
    # 删除一个Todo任务
    try:
        id = int(id)
    except:
        return 'id必须是int类型', 403

    database = get_database()
    for item in database:
        if id == item['id']:
            database.remove(item)
            set_database(database)
            return jsonify(database), 200
    return '删除失败，不存在id=%s的项' % (id), 404



if __name__ == "__main__":
    app.run(debug=True)
