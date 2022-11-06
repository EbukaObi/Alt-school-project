from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, LoginManager, UserMixin, current_user
import os
from datetime import datetime

base_dir = os.path.dirname(os.path.realpath(__file__))

db = SQLAlchemy()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(base_dir, 'blog.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = '5e0b18fd5de07e49f80cb4f8'

"""
To get a 12-digit (any number of choice) secret key, run this in the terminal:
python
import secrets
secrets.token_hex(12)
exit()
Copy the token from the terminal and paste it as the secret key in app.config above
"""

db.init_app(app)
login_manager = LoginManager(app)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    post = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now(), nullable=False)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f"User <{self.username}>"


with app.app_context():
    db.create_all()


@login_manager.user_loader
def user_loader(id):
    return User.query.get(int(id))


@app.route('/', methods=['GET'])
def home():
    blog = Blog.query.order_by(Blog.date_created.desc()).all()
    return render_template('index.html', blog=blog)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash("Logged in successfully.", category="success")
        else:
            flash("Invalid username or password.", category='error')
            return render_template('login.html')
        return redirect(url_for('home'))

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.")
    return redirect(url_for('home'))


@app.route('/protected')
@login_required
def protected():
    return render_template ('protected.html')


@app.route('/add_post', methods=['POST', 'GET'])
@login_required
def add_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        author = current_user.username
        date_created = datetime.now()
        new_post = Blog(title=title, post=content, author=author, date_created=date_created)
        with app.app_context():
            db.session.add(new_post)
            db.session.commit()
        flash("Your post has been created successfully!", "success")
        return redirect('/')

    return render_template('add_post.html')

@app.route('/add_post/<int:id>', methods=['GET', 'POST'])
def post_details(id):
    blog = Blog.query.get_or_404(id)
    date_created = datetime.now()
    return render_template('post_details.html', blog=blog)

@app.route('/add_post/<int:id>/edit', methods=['POST', 'GET'])
@login_required
def edit(id):
    edit_blog = Blog.query.get_or_404(id)

    if request.method == 'POST':
            edit_blog.title = request.form.get('title')
            edit_blog.post = request.form.get('content')
            edit_blog.date_created = datetime.now()
            with app.app_context():
                db.session.commit()
            flash("Your post has been updated successfully!", "success")

            return redirect(url_for('home'))

    return render_template('edit.html', edit_blog=edit_blog)



@app.route('/delete/<int:id>')
@login_required
def delete(id):
    delete_blog = Blog.query.get_or_404(id)
    with app.app_context():
        db.session.delete(delete_blog)
        db.session.commit()
    flash("Your post has been deleted successfully!", "error")
    return redirect(url_for('home'))


@app.route('/signup', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm')

        user = User.query.filter_by(username=username).first()

        if user:
            flash("Username already exists", 'error')
            return redirect(url_for('register'))
        elif password != confirm:
            flash('Passwords don\'t match', category='error')
            return redirect(url_for('register'))
        elif len(password) < 7:
            flash('Password must be at least 7 characters', category='error')
            return redirect(url_for('register'))
        else:
            flash('Account created!', category='success')

        password_hash = generate_password_hash(password)

        new_user = User(username=username, first_name=first_name, last_name=last_name, email=email, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
