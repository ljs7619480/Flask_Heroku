# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 01:00:17 2018

@author: linzino
"""

from flask import Flask, render_template
from flask_pymongo import PyMongo
import json

# class EntryEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, PyMongo.ObjectId):
#             return obj.__str__()
#         # Let the base class default method raise the TypeError
#         return json.JSONEncoder.default(self, obj)

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://104-2:nycuisgood@hackathon.ugeyw.mongodb.net/job"
mongo = PyMongo(app)

# @app.route("/")
# def hello():
#     return render_template('index.html')

#https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.find
@app.route("/job/<custno>/<next_job>")
def home_page(custno, next_job):
    data_cursor = mongo.db.processed_v5.find({"custno":custno, "next_job": next_job})
    data = list(data_cursor[:3])
    for d in data:
        d.pop("_id")

    return json.dumps(data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)