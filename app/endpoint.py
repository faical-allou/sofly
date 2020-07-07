from flask import render_template, jsonify
import requests
import os

from app import app

from back_end_config import *

if os.environ.get('ON_HEROKU'):
    dufftoken = os.environ.get("DUFFEL_TOKEN", default=False)
else :
    dufftoken = DUFFEL_TOKEN



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/test')
def search(): 
    
    url = 'https://api.duffel.com/air/offer_requests'
    header = {  "Accept-Encoding": "gzip",  "Accept": "application/json",  "Duffel-Version": "beta", "Authorization": "Bearer " + dufftoken}
    body = {"data": {"passengers": [{"type": "adult"}],"slices": [{"origin": "DFW","destination": "AUS","departure_date": "2020-10-24"}],"cabin_class": "economy"}}
    print(body)
    r = requests.post(url, headers=header, json=body)
    print(r)
    rjson = r.json()
    return rjson