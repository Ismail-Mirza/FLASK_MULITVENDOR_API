from src.helpers.models.base import BaseModel
from src.extension import db

class CartItem(BaseModel):
    """ CartItem Model class """

    __tablename__ = 'cart_items'

    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    product = db.relationship('Product', backref='product', lazy='joined')


class Cart(BaseModel):
    """ Cart Model class """

    __tablename__ = 'carts'

    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), unique=True, nullable=False)
    owner = db.relationship('User', backref='owner', lazy='joined')
    items = db.relationship('CartItem', backref='items', lazy='joined')
