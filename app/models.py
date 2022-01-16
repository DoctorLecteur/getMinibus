from app import db

class Stops(db.Model):
    __tablename__ = 'stops'

    id = db.Column(db.Integer, primary_key = True)
    name_stop = db.Column(db.String(256))
    width_map = db.Column(db.Float)
    longitude_map = db.Column(db.Float)

    def __init__(self, name_stop, width_map, longitude_map):
        self.name_stop = name_stop
        self.width_map = width_map
        self.longitude_map = longitude_map

    def __repr__(self):
        return f"{self.name_stop}:{self.width_map}:{self.longitude_map}"


class Routes(db.Model):
    __tablename__ = 'routes'

    route_id = db.Column(db.Integer, primary_key = True)
    start_stop = db.Column(db.Integer, db.ForeignKey('stops.id'))
    finish_stop = db.Column(db.Integer, db.ForeignKey('stops.id'))
    count_minibus = db.Column(db.Integer)
    count_stops = db.Column(db.Integer)

    def __init__(self, start_stop, finish_stop, count_minibus, count_stops):
        self.start_stop = start_stop
        self.finish_stop = finish_stop
        self.count_minibus = count_minibus
        self.count_stops = count_stops

    def __repr__(self):
        return f"{self.start_stop}:{self.finish_stop}:{self.count_minibus}:{self.count_stops}"

class StopRoute(db.Model):
    __tablename__ = 'stoproute'

    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('routes.route_id'))
    stop_id = db.Column(db.Integer, db.ForeignKey('stops.id'))

    def __init__(self, route_id, stop_id):
        self.route_id = route_id
        self.stop_id = stop_id

    def __repr__(self):
        return f"{self.route_id}:{self.stop_id}"
