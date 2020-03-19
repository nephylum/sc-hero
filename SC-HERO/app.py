from decouple import config
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv()

MONGO_URI = config('MONGO_URI')
ACCESS_KEY = config('ACCESS_KEY')
client = MongoClient(MONGO_URI)

def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = config('MONGO_URI')
    app.config['ACCESS_KEY'] = config('ACCESS_KEY')


    @app.route("/")
    def root():
        return "nothing here"

    @app.route(f"/{ACCESS_KEY}/singlecityWiki/<num>")
    def singlecityWiki(num):
        doc = client.SingleCity.WikiReal.find_one({'_id': int(num)})
        return jsonify(doc)

    @app.route(f"/{ACCESS_KEY}/wikisum/<num>")
    def wikisum(num):
        doc = client.SingleCity.wikidata.find_one({'_id': int(num)})
        return jsonify(doc)

    @app.route(f"/{ACCESS_KEY}/singlecityYelp/<num>")
    def singlecityYelp(num):
        doc = client.SingleCity.yelp_data.find_one({'_id': str(num)})
        return jsonify(doc)

    return app
