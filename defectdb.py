from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

db = SQLAlchemy()
ma = Marshmallow()


class Defect(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(15), unique=False)
    location = db.Column(db.String(50), unique=False)
    origin = db.Column(db.String(50), unique=False)
    type = db.Column(db.String(50), unique=False)
    cause = db.Column(db.String(50), unique=False)
    found = db.Column(db.String(50), unique=False)
    date = db.Column(db.String(10), unique=False)
    time = db.Column(db.String(10), unique=False)

    def __init__(self, serial_number, location, origin, type, cause, found):
        self.serial_number = serial_number
        self.location = location
        self.origin = origin
        self.type = type
        self.cause = cause
        self.found = found
        # d = datetime.utcnow()
        d = datetime.now()
        self.date = '{:%Y-%m-%d}'.format(d)
        self.time = '{:%H:%M}'.format(d)

    def __repr__(self) -> str:
        return super().__repr__()
        # return f'{self.serial_number}|{self.location}|{self.type}'


class DefectSchema(ma.Schema):
    class Meta:
        fields = ('id', 'serial_number', 'location', 'origin', 'type', 'cause', 'found', 'date', 'time')

class DefectManager():
    def __init__(self, app, db_name) -> None:
        # Database setup must be configured before db.init__app called
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        # 
        db.init_app(app)
        ma.init_app(app)

        # Add to Context Manager
        app.app_context().push()

        # Build the database
        #db.create_all()

    def save(self):
        db.session.commit()

    def add_defect(self, defect) -> None:
        # print(f'\nDefect to process: {defect}\n')
        serial_number = defect["serial_number"]
        location = defect["location"]
        origin = defect["origin"]
        type = defect["type"]
        cause = defect["cause"]
        found = defect["found"]
        new_defect = Defect(serial_number, location, origin, type, cause, found)
        # print(f'Defect Object: {new_defect}\n')
        db.session.add(new_defect)
        self.save()
        return new_defect.id

    def get_defects(self):
        all_defects = Defect.query.all()
        result = self.get_schema(has_many=True).dump(all_defects)
        # print(f'\nQueried Defects: {all_defects}\n')
        # print(f'Returned Schema: {result}\n')
        return result
    
    def get_defect(self, uid):
        # panel = Defect.query.filter_by(id=uid).first()
        panel = Defect.query.get(uid)
        return panel

    def delete(self, id):
        defect = self.get_defect(id)
        db.session.delete(defect)
        self.save()

    def delete_all(self):
        defects = Defect.query.all()
        for defect in defects:
            db.session.delete(defect)
        self.save()
    
    def get_schema(self, has_many=False):
        if has_many:
            return DefectSchema(many=True)
        else:
            return DefectSchema()

    def get_db(self):
        return db
    
    def schemed_json(self, defect):
        self.get_schema().jsonify(defect)
