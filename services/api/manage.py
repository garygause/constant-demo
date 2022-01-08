import os
import unittest

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
   db.session.add(Lender(1, "Apple Valley Inc", "100 Apple Lane", "Appleton", "WI", "54911", "9025551212"))
   db.session.add(Lender(2, "Industrial Heartland Credit Union", "1 Industrial Way", "Cleveland", "OH", "44101", "2165551212"))
   db.session.add(Lender(3, "Eastern Trust Company", "50 Wall Street", "New York", "NY", "10005", "9185551212"))
   db.session.add(Lender(4, "Golden National Bank", "561-A Main Street", "Golden", "CO", "80401", "3035551212"))
   db.session.add(Lender(5, "Island Lending", "100 Marginal Way", "Huntington", "NY", "11743", "6315551212"))

   db.session.add(Loan(1, 1, "Hui", "Zamorano", 0.075, 5000, 3197.35, 19, 48, 120.89, "05/31/2020"))
   db.session.add(Loan(2, 1, "Wilma", "Cecena", 0.05, 10000, 6278.40, 19, 48, 230.29, "05/31/2020"))

   db.session.add(Loan(7, 2, "Steve", "Alexander", 0.075, 20000, 12789.92, 19, 48, 483.58, "05/31/2020"))
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
