from app import db, ma

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
