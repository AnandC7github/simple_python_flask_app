'''App routes'''
from flask import render_template

from market import app
from market.model import Item
from market.forms import Form


@app.route("/")
@app.route("/home")
def hello():
    "hello world"
    return render_template("home.html")


@app.route("/market")
def market():
    "Market page"
    # items: list[dict] = [
    #     {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    #     {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    #     {'id': 3, 'name': 'Mobile', 'barcode': '231985128446', 'price': 150}
    # ]
    items = Item.query.all()
    return render_template("market.html", items=items)


# @app.route("/about/<user>")
# def about(user: str = 'user'):
#     "hello user | DYNAMIC ROUTE"
#     return f"hello {user}"


@app.route('/register')
def register_form():
    '''user registration route'''
    form = Form()
    return render_template('register.html', form=form)


