from flask import jsonify

from app.database.lender import Lender, LenderSchema
from app.database.loan import Loan, LoanSchema

def initialize_routes(app):

   lender_schema = LenderSchema()
   lenders_schema = LenderSchema(many=True)
   loan_schema = LoanSchema()
   loans_schema = LoanSchema(many=True)

   @app.route("/api")
   def test():
      """ replace this with swagger type doc """
      return jsonify(test="success")

   @app.route("/api/lenders")
   def lenders_list():
      lenders = Lender.query.all()
      response = jsonify(lenders_schema.dump(lenders))
      # just for now for development
      response.headers.add('Access-Control-Allow-Origin', '*')
      return response

   @app.route("/api/loans")
   def loans_list():
      loans = Loan.query.all()
      response = jsonify(loans_schema.dump(loans))
      # just for now for development
      response.headers.add('Access-Control-Allow-Origin', '*')
      return response

   @app.route("/api/loans/<int:lender_id>/")
   def loans_by_lender_id(lender_id):
      loans = Loan.query.filter(Loan.lender_id==lender_id).all()
      response = jsonify(loans_schema.dump(loans))
      # just for now for development
      response.headers.add('Access-Control-Allow-Origin', '*')
      return response

