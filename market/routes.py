'''App routes'''
from flask import render_template, redirect, url_for, flash,

from market import app, db
from market.model import Item, User
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


@app.route('/register', methods=['GET', 'POST'])
def register_form():
  '''user registration route'''
  form = Form()

  if form.validate_on_submit():
    print(form.username.data, "------")
    user_to_create=User(username=form.username.data,email=form.email.data,password=form.password.data)

    db.session.add(user_to_create)
    db.session.commit()
    return redirect('/market')
  if form.errors != {}: #if there are no error from validations
    for err_msg in form.errors.values():
      flash(f'There was an error in creating a user: {err_msg}')
  return render_template('register.html', form=form)
