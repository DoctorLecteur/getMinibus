# -*- coding: utf-8 -*-
from flask import render_template, make_response, request
from app import app, queries

QUERY_DB = queries.Query() #константа для модуля

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

@app.route('/stops', methods=['GET', 'POST'])
def get_route_stops():
    answer = {
        "httpcode": 200,
        "stops": []
    }

    if request.method == 'POST':
        stops_name = []

        route_id = request.get_json()['routeId']
        route = QUERY_DB.get_route(route_id)

        start_stop_name = QUERY_DB.get_name_stop(route.start_stop)
        finish_stop_name = QUERY_DB.get_name_stop(route.finish_stop)

        stops_name.append(start_stop_name)
        stops_name.append(finish_stop_name)

        answer["stops"] = stops_name
        return make_response(answer)