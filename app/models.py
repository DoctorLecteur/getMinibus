from app import db

class Stops(db.Model):
    __tablename__ = 'stops'

    id = db.Column(db.Integer, primary_key = True)
    name_stop = db.Column(db.String(256))
    width_map = db.Column(db.Float)
    longitude_map = db.Column(db.Float)
    direction = db.Column(db.String(32))

    def __init__(self, name_stop, width_map, longitude_map, direction):
        self.name_stop = name_stop
        self.width_map = width_map
        self.longitude_map = longitude_map
        self.direction = direction

    def __repr__(self):
        return f"<profiles {self.id}>"


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
        return f"<profiles {self.route_id}>"

class StopRoute(db.Model):
    __tablename__ = 'stoproute'

    id = db.Column(db.Integer, primary_key=True)
    route_id = db.Column(db.Integer, db.ForeignKey('routes.route_id'))
    stop_id = db.Column(db.Integer, db.ForeignKey('stops.id'))

    def __init__(self, route_id, stop_id):
        self.route_id = route_id
        self.stop_id = stop_id

    def __repr__(self):
        return f"<profiles {self.id}>"

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64))
    password = db.Column(db.String(256))
    save_route_id = db.Column(db.Integer, db.ForeignKey('routes.route_id'))
    save_stop_id = db.Column(db.Integer, db.ForeignKey('stops.id'))

    def __init__(self, login, password, save_route_id, save_stop_id):
        self.login = login
        self.password = password
        self.save_route_id = save_route_id
        self.save_stop_id = save_stop_id

    def __repr__(self):
        return f"<profiles {self.id}>"

