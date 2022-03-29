import json

from flask import Flask, jsonify, render_template, request
from flask_cors import cross_origin
from markupsafe import escape  # 用于转义 防止注入

import config
from exts import db
from model import *

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route("/hello")
@cross_origin(supports_credentials=True)
def myHello():
    return {
                'title':"How to use vue",
                'author':"Jane Doe",
                'publishedAt': "2016-04-10"
            }
@app.route("/fetchAll")
@cross_origin(supports_credentials=True)
def fetchAll():
    datas = model.index.query.all()
    print(datas)
    output = []
    for a,i in enumerate(datas):
        i = i.to_json()
        i['id'] = a
        print(i['chinese_titles'])
        print(i['titles'])
        i['chinese_titles'] = json.loads(i['chinese_titles'])
        i['titles'] = json.loads(i['titles'])
        output.append(i)
    return jsonify(output)
# 返回所有表的表名
@app.route("/fetchAllTableNames")
@cross_origin(supports_credentials=True)
def fetchAllTableNames():
    datas = index.query.with_entities(index.table_name, index.chinese_table_name).all()
    output = []
    for i in datas:
        output.append({'value': i['table_name'], 'label':i['chinese_table_name']})
    return jsonify(output)

# 返回一张表的表头信息
@app.route("/getTitles", methods=['GET'])
@cross_origin(supports_credentials=True)
def getTitles():
    print(request.args)
    tableName = request.args['tablename']
    datas = index.query.with_entities(index.titles, index.chinese_titles).filter(index.table_name==tableName).all()
    datas = datas[0]
    titles = json.loads(datas['titles'])
    chinese_titles = json.loads(datas['chinese_titles']) 
    print(titles)
    print(chinese_titles)
    output = [{'value':titles[i], 'label':chinese_titles[i]} for i in range(len(titles))]
    print(output)
    return jsonify(output)