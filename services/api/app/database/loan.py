from app import db, ma

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
