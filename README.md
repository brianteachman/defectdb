# Defect manager using Flask-SQLAlchemy's SQLite adapter

## Setup

Install virtual environment:

    > python -m venv venv

Activate virtual environment:

    > venv\Scripts\Activate.ps1

Install dependencies:

    (venv) > pip install -r requirements.txt

Run app: 

    (venv) > python app.py

Run test:

    (venv) > python -m unittest tests.py

If needed to create bundled package (dist); run Build:

    > py -m build

## References

- [SQLite](https://sqlite.org/cli.html)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/14/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) ([pip](https://pypi.org/project/Flask-SQLAlchemy/))
- [marshmellow](https://marshmallow.readthedocs.io/en/stable/) ([pip](https://flask-sqlalchemy.palletsprojects.com/en/2.x/))
- [Online SQLite Viewer](https://sqliteviewer.app/)
- [Flask Application Context](https://flask.palletsprojects.com/en/2.0.x/appcontext/)