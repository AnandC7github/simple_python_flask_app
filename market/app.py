# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# db = SQLAlchemy(app)


# class Item(db.Model):
#     """Data base table for ITEMS"""
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), nullable=False)
#     barcode = db.Column(db.String(), nullable=False)
#     price = db.Column(db.Integer(), nullable=False)
#     description = db.Column(db.String(), nullable=False)

#     def __repr__(self) -> str:
#         return f"ITEM < {self.name} | ${self.price} >"


# @app.route("/")
# @app.route("/home")
# def hello():
#     "hello world"
#     return render_template("home.html")


# @app.route("/market")
# def market():
#     "Market page"
#     # items: list[dict] = [
#     #     {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
#     #     {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
#     #     {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
#     # ]
#     items = Item.query.all()
#     return render_template("market.html", items=items)


# # @app.route("/about/<user>")
# # def about(user: str = 'user'):
# #     "hello user | DYNAMIC ROUTE"
# #     return f"hello {user}"



# if __name__ == "__main__":

#     with app.app_context():
#         # # create database and table
#         # db.create_all()

#         # # Add an item into the ITEM table
#         # item = Item(name='Phone', barcode='893212299897', price=500, description='Coolest phone ever')
#         # db.session.add(item)
#         # db.session.commit()

#         # # print all the items in the table ITEM
#         # print(Item.query.all())

#         # # Filter the query results 
#         for item in Item.query.filter_by(price=500):
#             print(">> ",item)


#     app.run(host="0.0.0.0", port=80, debug=True)


# # FLASK_APP = NAME OF Python file 
# # in windows  set FLASK_APP=app.py

# # DEBUG 
# # set FLASK_DEBUG=1
    
