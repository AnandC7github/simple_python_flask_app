from market import db


class Item(db.Model):
    """Data base table for ITEMS"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    barcode = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self) -> str:
        return f"ITEM < {self.name} | ${self.price} >"
