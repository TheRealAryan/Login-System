from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'oogaboogaStopLookingAtMyPassword'  # For session management
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

# User model for the database
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    display_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first() # Look up the user by email (I will implement logging in via username/email in the next update)

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('profile'))
        else:
            flash("Invalid credentials, please try again.", "danger")

    return render_template('login.html')

def validate_password(password):
    pattern = r'^(?=.*[A-Za-z])(?=.*\d).{8,}$' # At least one letter, one digit, 8 characters
    if re.match(pattern, password):
        return True
    return False

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email').lower()
        username = request.form.get('username').lower()
        display_name = request.form.get('display_name')
        password = request.form.get('password')
        repeat_password = request.form.get('repeat_password')

        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$' # Email validation
        if not re.match(email_regex, email):
            flash("Invalid email format!", "danger")
            return render_template('register.html')

        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash("Email already exists! Please choose a different email or login.", "danger")
            return render_template('register.html')

        username_regex = r'^[a-zA-Z0-9_]+$'  # Only alphanumeric characters and underscores
        if not re.match(username_regex, username):
            flash("Username can only contain letters, numbers, and underscores (no spaces or special characters).", "danger")
            return render_template('register.html')

        existing_username = User.query.filter_by(username=username).first()
        if existing_username:
            flash("Username already taken! Please choose a different username.", "danger")
            return render_template('register.html')

        if password != repeat_password:
            flash("Passwords don't match!", "danger")
            return render_template('register.html')

        if not validate_password(password):
            flash("Password must be at least 8 characters long, include at least one letter and at least one digit.", "danger")
            return render_template('register.html')
        
        hashed_password = generate_password_hash(password)

        new_user = User(email=email, username=username, display_name=display_name, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully! You can now log in.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/profile')
@login_required  # User must be logged in to view the profile
def profile():
    return render_template('profile.html', user=current_user)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    if request.method == 'POST':
        logout_user()
        return redirect(url_for('home'))
    return redirect(url_for('profile'))

if __name__ == '__main__':
    app.run(debug=True)
