from run import db

# Products
class Products(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    product_categ=db.Column(db.String(70))
    product_price=db.Column(db.String(100))
    product_image=db.Column(db.String(50))