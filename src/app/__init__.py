'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Team: BadButter
Description: Project 1 - Sol Systems Web App
'''

import bcrypt
from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os, uuid, datetime

app = Flask("Authentication Web App")
app.secret_key = 'do not share'
app.config['USER SIGN UP']= 'User Sign Up"'
app.config['USER SIGNIN']= 'User Sign In"'
csrf = CSRFProtect()
csrf.init_app(app)

# cache setup
from flask_caching import Cache
cache = Cache()
cache.init_app(app, config={
    'CACHE_TYPE': 'simple',
    'CACHE_DEFAULT_TIMEOUT': 5
})

# db initialization
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)


from app import models
with app.app_context(): 
    db.create_all()

# login manager
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

from app.models import User

# user_loader callback
@login_manager.user_loader
def load_user(id):
    try: 
        return db.session.query(User).filter(User.id==id).one()
    except: 
        return None

# create initial required data for grading stuff
from app.routes import simulate
simulate()

from app.models import Event, Task
with app.app_context():
    print("tmota admin creation needed" if User.query.filter_by(id = 'tmota').first() is None else "tmota admin exists")
    if User.query.filter_by(id = 'tmota').first() is None:
        hash_password = bcrypt.hashpw('1'.encode('utf-8'), bcrypt.gensalt())  # Hash the password
        TMota = User(
            id = 'tmota',
            password = hash_password,
        )

        hash_password = bcrypt.hashpw('1'.encode('utf-8'), bcrypt.gensalt())  # Hash the password
        TUser = User(
            id = 'test user',
            password = hash_password,
        )

        start_time = datetime.datetime.now() + datetime.timedelta(days=1, hours=3)
        end_time = datetime.datetime.now() + datetime.timedelta(days=1, hours=5)
        e1 = Event(
            id = str(uuid.uuid4()),
            type = 'event',
            user_id = 'tmota',
            title = 'Test',
            start_time = start_time,
            end_time = end_time,
            date = datetime.datetime.today(),
            notes = 'this is the 1st event!',
        )

        start_time = datetime.datetime.now() + datetime.timedelta(days=1, hours=4)
        end_time = datetime.datetime.now() + datetime.timedelta(days=1, hours=7)
        print(start_time.timetz())
        print(start_time.timetz().strftime("%H:%M"))
        e2 = Event(
            id = str(uuid.uuid4()),
            type = 'event',
            user_id = 'tmota',
            title = 'Test2',
            start_time = start_time,
            end_time = end_time,
            date = datetime.datetime.today(),
            notes = 'this is the 2nd event!',
        )

        start_time = datetime.datetime.now() + datetime.timedelta(days=1, hours=8)
        end_time = datetime.datetime.now() + datetime.timedelta(days=1, hours=9)
        e3 = Event(
            id = str(uuid.uuid4()),
            type = 'event',
            user_id = 'tmota',
            title = 'Test3',
            start_time = start_time,
            end_time = end_time,
            date = datetime.datetime.today(),
            notes = 'this is the 3rd event!',
        )

        start_time = datetime.datetime.now() + datetime.timedelta(days=1, hours=11)
        end_time = datetime.datetime.now() + datetime.timedelta(days=1, hours=13)
        e4 = Event(
            id = str(uuid.uuid4()),
            type = 'event',
            user_id = 'tmota',
            title = 'Test4',
            start_time = start_time,
            end_time = end_time,
            date = datetime.datetime.today(),
            notes = 'this is the 4th event!',
        )

        start_time = datetime.datetime.now() + datetime.timedelta(days=0, hours=2)
        end_time = datetime.datetime.now() + datetime.timedelta(days=0, hours=2)
        e5 = Event(
            id = str(uuid.uuid4()),
            type = 'event',
            user_id = 'tmota',
            title = 'Test5',
            start_time = start_time,
            end_time = end_time,
            date = datetime.datetime.today(),
            notes = 'this is the 5th event!',
        )

        start_time = datetime.datetime.now() + datetime.timedelta(days=1, hours=11)
        t1 = Task(
            id = str(uuid.uuid4()),
            type = 'task',
            user_id = 'tmota',
            title = 'Test4',
            start_time = start_time,
            is_complete = False,
            date = datetime.datetime.today(),
            notes = 'this is the 1st task!',
        )

        start_time = datetime.datetime.now() + datetime.timedelta(days=1, hours=16)
        t2 = Task(
            id = str(uuid.uuid4()),
            type = 'task',
            user_id = 'tmota',
            title = 'Test4',
            start_time = start_time,
            is_complete = False,
            date = datetime.datetime.today(),
            notes = 'this is the 2nd task!',
        )

        start_time = datetime.datetime.now() + datetime.timedelta(days=0, hours=1)
        t3 = Task(
            id = str(uuid.uuid4()),
            type = 'task',
            user_id = 'tmota',
            title = 'Test4',
            start_time = start_time,
            is_complete = False,
            date = datetime.datetime.today(),
            notes = 'this is the 3rd task!',
        )

        # This one should get rescheduled instantly
        start_time = datetime.datetime.now() + datetime.timedelta(days=0, hours=0)
        t4 = Task(
            id = str(uuid.uuid4()),
            type = 'task',
            user_id = 'tmota',
            title = 'Test4',
            start_time = start_time,
            is_complete = False,
            date = datetime.datetime.today(),
            notes = 'this is the 4th task!',
        )

        start_time = datetime.datetime.now() + datetime.timedelta(days=0, hours=2)
        t5 = Task(
            id = str(uuid.uuid4()),
            type = 'task',
            user_id = 'tmota',
            title = 'Test5',
            start_time = start_time,
            is_complete = False,
            date = datetime.datetime.today(),
            notes = 'this is the 5th task!',
        )

        start_time = datetime.datetime.now() + datetime.timedelta(days=0, hours=3)
        t6 = Task(
            id = str(uuid.uuid4()),
            type = 'task',
            user_id = 'tmota',
            title = 'Test6',
            start_time = start_time,
            is_complete = False,
            date = datetime.datetime.today(),
            notes = 'this is the 6th task!',
        )

        start_time = datetime.datetime.now() + datetime.timedelta(days=0, hours=4)
        t7 = Task(
            id = str(uuid.uuid4()),
            type = 'task',
            user_id = 'tmota',
            title = 'Test7',
            start_time = start_time,
            is_complete = False,
            date = datetime.datetime.today(),
            notes = 'this is the 7th task!',
        )

        print(t2.id)

        db.session.add(TMota)
        db.session.add(TUser)
        db.session.add(e1)
        db.session.add(e2)
        db.session.add(e3)
        db.session.add(e4)
        db.session.add(e5)
        db.session.add(t1)
        db.session.add(t2)
        db.session.add(t3)
        db.session.add(t4)
        db.session.add(t5)
        db.session.add(t6)
        db.session.add(t7)
        db.session.commit()

from app import routes