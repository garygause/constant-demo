from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object("app.config.Config")
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Lender(db.Model):
   """ Lender Model """
   __tablename__ = "lenders"

   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(128), nullable=False)
   address = db.Column(db.String(255))
   city = db.Column(db.String(128))
   state = db.Column(db.String(2))
   zip = db.Column(db.String(10))
   phone = db.Column(db.String(16))
   #loans = db.relationship('Loan', backref='Lender', lazy=True)

   def __init__(self, id, name, address, city, state, zip, phone):
      self.id = id
      self.name = name
      self.address = address
      self.city = city
      self.state = state
      self.zip = zip
      self.phone = phone

   def __repr__(self):
      return "<Lender '{}'>".format(self.name)


class LenderSchema(ma.SQLAlchemyAutoSchema):
   class Meta:
      model = Lender
      include_fk = True


class Loan(db.Model):
   """ Loan Model """
   __tablename__ = "loans"

   id = db.Column(db.Integer, primary_key=True)
   first_name = db.Column(db.String(255))
   last_name = db.Column(db.String(255))
   interest_rate = db.Column(db.Float)
   loan_amount = db.Column(db.Integer)
   current_balance = db.Column(db.Float)
   number_payments = db.Column(db.Integer)
   loan_term = db.Column(db.Integer)
   monthly_payment = db.Column(db.Float)
   contract_date = db.Column(db.Date)
   lender_id = db.Column(db.Integer, nullable=False)
   #lender_id = db.Column(db.Integer, db.ForeignKey('lender.id'), 
   #   nullable=False)

   def __init__(self, id, lender_id, first_name, last_name, interest_rate, loan_amount, current_balance, number_payments, loan_term, monthly_payment, contract_date):
      self.id = id
      self.lender_id = lender_id
      self.first_name = first_name
      self.last_name = last_name
      self.interest_rate = interest_rate
      self.loan_amount = loan_amount
      self.current_balance = current_balance
      self.number_payments = number_payments
      self.loan_term = loan_term
      self.monthly_payment = monthly_payment
      self.contract_date = contract_date  


class LoanSchema(ma.SQLAlchemyAutoSchema):
   class Meta:
      model = Loan
      include_fk = True


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
