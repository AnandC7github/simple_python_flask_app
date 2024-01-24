from market import app, db, Item

# Run the flask app

if __name__ == "__main__":

    with app.app_context():
        # create database and table
        # db.create_all()

        # Add an item into the ITEM table
        # item = Item(name='Phone', barcode='893212299897', price=500, description='Coolest phone ever')
        # db.session.add(item)
        # db.session.commit()

        # # print all the items in the table ITEM
        # print(Item.query.all())

        # # Filter the query results 
        for item in Item.query.filter_by(price=500):
            print(">> ",item)


    app.run(host="0.0.0.0", port=80, debug=True)


# FLASK_APP = NAME OF Python file 
# in windows  set FLASK_APP=app.py

# DEBUG 
# set FLASK_DEBUG=1