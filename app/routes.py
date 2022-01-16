# -*- coding: utf-8 -*-
from flask import render_template, make_response
from app import app

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/stops', methods=['GET', 'POST'])
def get_route_stops():
    print("stops - 1,2,3")
    return make_response()