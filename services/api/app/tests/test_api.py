from copy import deepcopy
import unittest
import json

from app import app, db

BASE_URL = "http://localhost:3000/api"
LENDERS_URL = "{}/lenders".format(BASE_URL)
LENDER_LOAN_URL = "{}/loans/1/".format(BASE_URL)
BAD_LENDER_LOAN_URL = "{}/loans/5555/".format(BASE_URL)
LOANS_URL = "{}/loans".format(BASE_URL)


class TestAPI(unittest.TestCase):

   def seed_db():

      # TODO: move lender sample data to external file
      db.session.add(Lender(1, "Apple Valley Inc", "100 Apple Lane", "Appleton", "WI", "54911", "9025551212"))
      db.session.add(Lender(2, "Industrial Heartland Credit Union", "1 Industrial Way", "Cleveland", "OH", "44101", "2165551212"))
      db.session.add(Lender(3, "Eastern Trust Company", "50 Wall Street", "New York", "NY", "10005", "9185551212"))
      db.session.add(Lender(4, "Golden National Bank", "561-A Main Street", "Golden", "CO", "80401", "3035551212"))
      db.session.add(Lender(5, "Island Lending", "100 Marginal Way", "Huntington", "NY", "11743", "6315551212"))

      try:
         with open('../sample_data/loans.csv', newline='') as f:
             reader = csv.reader(f)
             for row in reader:
                 db.session.add(Loan(
                    int(row[0]), int(row[1]), row[2], row[3], float(row[4]), int(row[5]), 
                    float(row[6]), int(row[7]), int(row[8]), float(row[9]), row[10]
                 ))
      except:
         # TODO: add logging for errors
         pass
      
      db.session.commit()


   def setUp(self):
      self.app = app.test_client()
      self.app.testing = True

   def test_get_lenders(self):
      response = self.app.get(LENDERS_URL)
      data = json.loads(response.get_data())
      self.assertEqual(len(data), 5)

   def tearDown(self):
      pass

