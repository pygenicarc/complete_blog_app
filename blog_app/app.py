from flask import Flask, render_template, request, redirect
from utils.db import db
from models.blog import *


flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'


@flask_app.route('/')
def index():
    blogs = Blog.query.all()
    return render_template('index.html', content=blogs)


@flask_app.route('/about')
def about():
    return render_template('about.html')


@flask_app.route('/blogs')
def blogs():
    blogs_list = [
        {
            "blog_id":1,
            "blog_title":"blog one",
            "blog_content":"blog dummy content",
            "author":"Author 1",
            "date":"28/11/2024"
         },
        {
            "blog_id": 2,
            "blog_title": "blog one",
            "blog_content": "blog dummy content",
            "author": "Author 1",
            "date": "28/11/2024"
        },
        {
            "blog_id": 3,
            "blog_title": "blog one",
            "blog_content": "blog dummy content",
            "author": "Author 1",
            "date": "28/11/2024"
        },
        {
            "blog_id": 4,
            "blog_title": "blog one",
            "blog_content": "blog dummy content",
            "author": "Author 1",
            "date": "28/11/2024"
        },
        {
            "blog_id": 5,
            "blog_title": "blog one",
            "blog_content": "blog dummy content",
            "author": "Author 1",
            "date": "28/11/2024"
        },
        {
            "blog_id": 6,
            "blog_title": "blog one",
            "blog_content": "blog dummy content",
            "author": "Author 1",
            "date": "28/11/2024"
        },
    ]
    return render_template('blogs.html', blogs=blogs_list)


@flask_app.route('/add-blog')
def add_blog():
    return render_template('add_blog.html')


db.init_app(flask_app)


with flask_app.app_context():
    db.create_all()


@flask_app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form.to_dict()
    print(f"form_data: {form_data}")

    author_name = form_data.get('author_name')
    author_email = form_data.get('author_email')
    author_mobile = form_data.get('author_mobile')
    author_address = form_data.get('author_address')

    blog_title = form_data.get('blog_title')
    blog_content = form_data.get('blog_content')
    blog_date = form_data.get('blog_date')

    author = Author.query.filter_by(email=author_email).first()
    if not author:
        author = Author(name=author_name, email=author_email, mobile=author_mobile, address=author_address)
        db.session.add(author)
        db.session.commit()

    blog = Blog(blog_title=blog_title, blog_content=blog_content, date=blog_date, author_id=author.id)
    db.session.add(blog)
    db.session.commit()
    print("sumitted successfully")
    return redirect('/')


if __name__ == '__main__':
    flask_app.run(
        host='127.0.0.1',
        port=8005,
        debug=True
    )