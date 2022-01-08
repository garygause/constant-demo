import os
import unittest
import csv

from flask.cli import FlaskGroup

from app import app, db, Lender, Loan

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
   db.drop_all()
   db.create_all()
   db.session.commit()

@cli.command("seed_db")
def seed_db():

   # TODO: move lender sample data to external file
   db.session.add(Lender(1, "Apple Valley Inc", "100 Apple Lane", "Appleton", "WI", "54911", "9025551212"))
   db.session.add(Lender(2, "Industrial Heartland Credit Union", "1 Industrial Way", "Cleveland", "OH", "44101", "2165551212"))
   db.session.add(Lender(3, "Eastern Trust Company", "50 Wall Street", "New York", "NY", "10005", "9185551212"))
   db.session.add(Lender(4, "Golden National Bank", "561-A Main Street", "Golden", "CO", "80401", "3035551212"))
   db.session.add(Lender(5, "Island Lending", "100 Marginal Way", "Huntington", "NY", "11743", "6315551212"))

   try:
      with open('./loans.csv', newline='') as f:
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

@cli.command("run_tests")
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == "__main__":
   cli()
