from flask import render_template, jsonify
import requests
import os
import psycopg2

from app import app

from back_end_config import *
from models.extractdata import *


if os.environ.get('ON_HEROKU'):
    dufftoken = os.environ.get("DUFFEL_TOKEN", default=False)
else :
    dufftoken = DUFFEL_TOKEN

extractdata = extractdata()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/test')
def search_duffel():  
    url = 'https://api.duffel.com/air/offer_requests'
    h_ = {  "Accept-Encoding": "gzip",  "Accept": "application/json",  "Duffel-Version": "beta", "Authorization": "Bearer " + dufftoken}
    b_ = {"data": {"passengers": [{"type": "adult"}],"slices": [{"origin": "DFW","destination": "AUS","departure_date": "2020-10-24"}],"cabin_class": "economy"}}
    print(b_)
    r = requests.post(url, headers=h_, json=b_)
    print(r)
    rjson = r.json()
    return rjson

@app.route('/test2')
def search_kiwi():  
    url = 'https://tequila-api.kiwi.com/v2/search?fly_from=PRG&fly_to=LON&dateFrom=18/11/2020&dateTo=12/12/2020'
    h_ = {  "Accept-Encoding": "gzip",  "Accept": "application/json",  "apikey": kiwi_apikey}
    print(h_)
    r = requests.get(url, headers=h_)
    print(r)
    rjson = r.json()
    return rjson

@app.route('/check')
def check():
    check_flight = extractdata.getflight('abc')
    return check_flight

@app.route('/webhook',methods=['GET', 'POST'])
def read_stuff():
    json_request = request.get_json(force=True, silent=False, cache=True)
    print(json_request)
    return json_request