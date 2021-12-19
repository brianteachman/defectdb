import unittest
import os

from flask import Flask
from defectdb import DefectManager

basedir = os.path.abspath(os.path.dirname(__file__))
db_file = os.path.join(basedir + os.path.sep + "test.sqlite")

test_defect = {
    "serial_number":"202112041314w",
    "location":"A10",
    "origin":"Stringer 3",
    "type":"Missed Solder (MS)",
    "cause":"Machine",
    "found":"Post-Solder (QC2)",
    "date":"11/0/2021",
    "time":"2:29 AM",
}


class TestDefectManager(unittest.TestCase):

    def setUp(self):
        super().setUp()
        # DefectManager requires the Flask app to setup and initialize integration
        self.app = Flask(__name__)
        self.db = DefectManager(self.app, db_file)

    def tearDown(self):
        self.db._get_db().session.close()
        super().tearDown()

    def test_add_defect(self):
        id = self.db.add_defect(test_defect)
        self.assertEqual(self.db.get_defect(id).id, id, 'incorrect Defect ID')


if __name__ == '__main__':
    unittest.main()
