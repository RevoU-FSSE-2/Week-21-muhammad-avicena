from flask import Flask
from app.auth.apis import auth_blueprint
from app.user.apis import user_blueprint
from app.home.apis import home_blueprint
from app.tweet.apis import tweet_blueprint
from infrastructure.db import db, db_init
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db.init_app(app)

app.register_blueprint(home_blueprint, url_prefix="/")
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(user_blueprint, url_prefix="/user")
app.register_blueprint(tweet_blueprint, url_prefix="/tweet")

# with app.app_context():
#     db_init()
