import json

import pymysql
from flask import (Flask, jsonify, make_response, render_template, request,
                   send_from_directory)
from flask_cors import cross_origin
from markupsafe import escape  # 用于转义 防止注入
import sqlGenerator
import csv
import pandas as pd# 还需要openpyxl

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
    datas = index.query.all()
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

@app.route("/getExcel", methods=['POST'])
@cross_origin(supports_credentials=True)
def getExcel():
    # 获取Post请求头
    postData = request.get_json()
    print(postData)
    
    try:
        # 构建pymysql链接：
        db = pymysql.connect(
            host = config.TARGETHOST,
            user = config.TARGETUSER,
            password= config.TARGETPASSWORD,
            database= config.TARGETDATABASE,
            port=config.TARGETPORT
            )
        
        cursor = db.cursor()
        title, sql = sqlGenerator.parseToSQL(postData, 'ID') # 利用生成器获取对应的sql语句
        print(sql)
        cursor.execute(sql)
        results= cursor.fetchall()
        # 先暂存到csv文件，再保存到xlsx
        with open('./cache/temp.csv', 'w',newline="") as f:
            writer = csv.writer(f)
            writer.writerow(title)
            writer.writerows(results)

        df = pd.read_csv("./cache/temp.csv",encoding='GBK')
        print(df)
        df.to_excel("./cache/temp.xlsx", sheet_name='sheet1',encoding='GB2312', index=None)

        print('---------------------------')

        print("----------------------------")
        db.close()
    except BaseException as err:
        print("ERROR: {}".format(err))
        


    # return jsonify(postData)
    with open('./cache/temp.xlsx','rb') as f:
        data = f.read()
        res = make_response(data)
        res.headers['Content-Type'] = 'image/jpeg'
         
    # with open('./cache/a.txt','rb') as f:
    #     data = f.read()
    #     res = make_response(data)
    #     # res.headers['Content-Type'] = 'image/jpeg'
    #     print(res.headers)    
        return res
