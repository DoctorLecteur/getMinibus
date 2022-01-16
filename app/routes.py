# -*- coding: utf-8 -*-
from flask import render_template, make_response, request
from app import app, db, models

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
        try:
            routes = models.Routes.query.filter_by(route_id = request.form.get('routeId')).all()
            for i in range(0, len(routes), 1):
                start_stop = models.Stops.query.filter_by(id = routes[i].start_stop).all()[0].name_stop
                finish_stop = models.Stops.query.filter_by(id=routes[i].finish_stop).all()[0].name_stop
                stops_name.append(start_stop)
                stops_name.append(finish_stop)
        except:
            print("Ошибка чтения БД")

        answer["stops"] = stops_name
        return make_response(answer)