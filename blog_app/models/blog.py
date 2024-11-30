from utils.db import db


# parent table
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    #
    blogs = db.relationship('Blog', backref='author', lazy=True)

# child table
class Blog(db.Model):
    blog_id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(100), nullable=False)
    blog_content = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
