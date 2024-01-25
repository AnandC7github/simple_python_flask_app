'''SQLlite Model '''
from market import db, app


class User(db.Model):
  """Database table for USERS"""
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(30), nullable=False)
  email = db.Column(db.String(60), nullable=False)
  password = db.Column(db.String(60), nullable=False)
  budget = db.Column(db.Integer(), nullable=False, default=1000)
  items = db.relationship("Item", backref='owned_user', lazy=True)

  def __repr__(self) -> str:
    return f"USER [ {self.username} ]"


class Item(db.Model):
  """Database table for ITEMS"""
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(30), nullable=False)
  barcode = db.Column(db.String(), nullable=False)
  price = db.Column(db.Integer(), nullable=False)
  description = db.Column(db.String(), nullable=False)
  owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

  def __repr__(self) -> str:
    return f"ITEM < {self.name} | ${self.price} >"


# set up database, table ..

with app.app_context():
  # # drop the database tables
  db.drop_all()
  # # create database and table
  db.create_all()

  # # Add an item into the ITEM table
  item = Item(name='Phone',
              barcode='893212299897',
              price=500,
              description='Coolest phone ever')
  db.session.add(item)
  db.session.commit()

  # # Add an user into the USER table
  user_1 = User(username='ajay', password='123456', email='ajay@gmail.com')
  db.session.add(user_1)
  db.session.commit()

  # # print all the items in the table ITEM
  # print(Item.query.all())

  # # Filter the query results
  for item in Item.query.filter_by(price=500):
    print(">> ", item)

  for user in User.query.all():
    print("--> ", user)

  # # db.session.rollback --> rollback previous changes and commits

  # # Assign product to a user
  item_1 = Item.query.filter_by(price=500).first()
  # # user you want -- get the id
  user_1_id = User.query.filter_by(username='ajay').first().id
  # # update product info
  item_1.owner = user_1_id
  db.session.add(item_1)
  db.session.commit()

  print("USER ID", user_1_id)
  # # Filter the query results
  for item in Item.query.filter_by(owner=user_1_id):
    print(">> ", item, " << ", item.owner)
