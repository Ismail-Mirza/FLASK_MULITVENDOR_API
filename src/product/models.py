from src.models.base import BaseModel
from src.extension import db


class Brand(BaseModel):
    """ Brand Model class """

    __tablename__ = 'brands'

    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    products = db.relationship(
        'Product', backref='brand_products', lazy='joined')


class Category(BaseModel):
    """ Category Model class """

    __tablename__ = 'categories'

    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    parent_id = db.Column(db.Integer, db.ForeignKey(
        'categories.id', ondelete='SET NULL'), nullable=True)
    products = db.relationship(
        'Product', cascade='all, delete-orphan', backref='category_products', lazy='joined')

class Product(BaseModel):
    """ Product Model class """

    __tablename__ = 'products'

    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    # main_image = db.Column(JSON, nullable=False)
    # images = db.Column(ARRAY(JSON), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey(
        'categories.id'), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey(
        'brands.id', ondelete='SET NULL'), nullable=True)
    price = db.Column(db.DECIMAL(12, 2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    rating = db.Column(db.Integer,nullable=False,default=0)

