from copy import deepcopy
import unittest
import json

import app

BASE_URL = "http://localhost:3000/api"
LENDERS_URL = "{}/lenders".format(BASE_URL)
LENDER_LOAN_URL = "{}/loans/1/".format(BASE_URL)
BAD_LENDER_LOAN_URL = "{}/loans/5555/".format(BASE_URL)
LOANS_URL = "{}/loans".format(BASE_URL)


class TestAPI(unittest.TestCase):

   def setUp(self):
      self.app = app.app.test_client()
      self.app.testing = True

   def test_get_lenders(self):
      response = self.app.get(LENDERS_URL)
      data = json.loads(response.get_data())
      self.assertEqual(len(data), 5)

   def tearDown(self):
      pass

