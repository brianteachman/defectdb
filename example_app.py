import os
from flask import Flask, request, jsonify
from defectdb import DefectManager

app = Flask(__name__)

# Get path to sqlite database (defects.sqlite)
basedir = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(basedir + os.path.sep + "data" + os.path.sep + "defects.sqlite")
# 
db = DefectManager(app, db_file)
# 
print(f'\nOpened database: {db_file}\n')

# Display all defects, JSON formatted
@app.route("/", methods=["GET"])
def home_page():
    defects = db.get_defects()
    return jsonify(defects)

# Endpoint for querying a single defect
@app.route("/defect/<id>", methods=["GET"])
def read_defect(id):
    defect = db.get_defect(id)
    return db.schemed_json(defect)

# Endpoint to create a new defect
@app.route('/defect', methods=["POST"])
def create_defect():
    print(f'{request.json}\n')
    uid = db.add_defect(request.json)
    defect = db.get_defect(uid)
    return db.schemed_json(defect)

# Endpoint for updating a defect
@app.route("/defect/<id>", methods=["PUT"])
def update_defect(id):
    defect = db.get_defect(id)
    db.update(defect, request.json)
    return db.schemed_json(defect)

# TODO: Remove this from production.
@app.route("/delete", methods=["GET"])
def delete_table():
    db.delete_all()
    return jsonify("BOMBED da tables!!")

# Endpoint for deleting a record
@app.route("/defect/<id>", methods=["DELETE"])
def delete_defect(id):
    db.delete(id)
    return f"Entry #{id} was successfully deleted"


if __name__ == '__main__':
    app.run(debug=True)
