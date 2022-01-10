import unittest
import json

from app import app, db
from app.database.loan import Loan

BASE_URL = "http://localhost:3000/api"
LOANS_URL = "{}/loans".format(BASE_URL)


class TestAPI(unittest.TestCase):

   def setUp(self):
      self.app = app.test_client()
      self.app.testing = True

   def test_get_loans(self):
      """
       test get loans from api

       let's pretend we have a test db setup and insert some test data
       then query the api and remove test data.
       api requirements do not include inserting data through api.
      """

      db.session.add(Loan(9999, 9998, 'Test Name', 'Test Last', 0.075, 4000, 3000.10, 12, 14, 333.33, "05/20/2020"))
      db.session.commit()

      response = self.app.get(LOANS_URL)
      data = json.loads(response.get_data())
      self.assertEqual(len(data), 34)

      db.session.query(Loan).filter(Loan.id==9999).delete()
      db.session.commit()

   def test_get_loans_by_lender(self):
      """
       test get loans by lender from api

       let's pretend we have a test db setup and insert some test data
       then query the api and remove test data.
       api requirements do not include inserting data through api.
      """

      db.session.add(Loan(9999, 9998, 'Test Name', 'Test Last', 0.075, 4000, 3000.10, 12, 14, 333.33, "05/20/2020"))
      db.session.commit()

      response = self.app.get("{}/9998/".format(LOANS_URL))
      data = json.loads(response.get_data())
      self.assertEqual(len(data), 1)
      self.assertEqual(data[0]['id'], 9999)

      db.session.query(Loan).filter(Loan.id==9999).delete()
      db.session.commit()

   def tearDown(self):
      pass

