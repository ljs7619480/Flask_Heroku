# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 01:00:17 2018

@author: linzino
"""

from flask import Flask, render_template
from flask_pymongo import PyMongo
import csv

# class EntryEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, PyMongo.ObjectId):
#             return obj.__str__()
#         # Let the base class default method raise the TypeError
#         return json.JSONEncoder.default(self, obj)

app = Flask(__name__,
            static_url_path='/', 
            static_folder='web/static',
            template_folder='web/templates')
app.config["MONGO_URI"] = "mongodb+srv://104-2:nycuisgood@hackathon.ugeyw.mongodb.net/job"
mongo = PyMongo(app)

dist_map = {}
with open('104/category/district.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file,)
    title  = csv_reader.fieldnames
    for row in csv_reader.reader:
        dist_map[int(row[0])] = row[1]



@app.route("/")
def hello():
    return render_template('job.html')

@app.route("/mont")
def hello():
    return render_template('mont.html')

@app.route("/tgetet")
def hello():
    return render_template('tgetet.html')

#https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.find
@app.route("/job/<custno>/<jobno>")
def home_page(custno, jobno):
    data_cursor = mongo.db.processed_v5.find({"custno":custno, "jobno": jobno})
    data = list(data_cursor[:3])
    for d in data:
        d.pop("_id")

    return render_template('index104.html', 
                           next_job=data[0]['next_job'],
                           district=dist_map[data[0]['addr_no']])


@app.route("/store")
def hello():
    return render_template('store.html')

@app.route("/movie")
def hello():
    return render_template('movies.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
