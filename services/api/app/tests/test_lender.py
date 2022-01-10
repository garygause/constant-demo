import unittest
import json

from app import app, db
from app.database.lender import Lender

BASE_URL = "http://localhost:3000/api"
LENDERS_URL = "{}/lenders".format(BASE_URL)


class TestAPI(unittest.TestCase):

   def setUp(self):
      self.app = app.test_client()
      self.app.testing = True

   def test_get_lenders(self):
      """
       test get lenders from api

       let's pretend we have a test db setup and insert some test data
       then query the api and remove test data.
       api requirements do not include inserting data through api.
      """

      db.session.add(Lender(9999, "Test Lending", "100 Marginal Way", "Huntington", "NY", "11743", "6315551212"))
      db.session.commit()

      response = self.app.get(LENDERS_URL)
      data = json.loads(response.get_data())
      self.assertEqual(len(data), 6)

      db.session.query(Lender).filter(Lender.id==9999).delete()
      db.session.commit()

      # verify db is back in demo state with our data removed
      # normally we'd wipe out the db so it is back in a pristine state
      response = self.app.get(LENDERS_URL)
      data = json.loads(response.get_data())
      self.assertEqual(len(data), 5)


   def tearDown(self):
      pass

