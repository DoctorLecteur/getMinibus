from app import models

#константы для классов БД
ROUTES = models.Routes
STOPS = models.Stops

class Query(object):

    def __init__(self):
        pass

    def get_route(self, route_id):
        route = ROUTES.query.filter_by(route_id = route_id).all()
        if (route):
            return route[0]
        else:
            print("Маршрут не найден!")

    def get_stop(self, stop_id):
        stop = STOPS.query.filter_by(id = stop_id).all()
        if (stop):
            return stop[0]
        else:
            print("Остановка не найдена")

    def get_name_stop(self, stop_id):
        stop = self.get_stop(stop_id)
        if (stop):
            return stop.name_stop
        else:
            print("Остановка маршрута не найдена")
