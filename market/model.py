from market import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(length=30), nullable=False, unique = True)
  email_address = db.Column(db.String(length=50), nullable=False, unique = True)
  password_hashed = db.Column(db.String(length=60), nullable=False)
  budget = db.Column(db.Integer(), nullable=False, default=1000)
  items = db.relationship('Item', backref = 'owned_user',lazy=True)

class Item(db.Model):
    """Data base table for ITEMS"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    barcode = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
  
    def __repr__(self) -> str:
        return f"ITEM < {self.name} | ${self.price} >"
