from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
app = Flask(__name__)




nav = Nav()

@nav.navigation()
def mynavbar():
    return Navbar(
        'K-Smart',
        View('Home', 'index'),
        View('Login', 'login'),
        View('Devices', 'device', name='0'),
        View('Condition', 'cond'),
        View('Camera', 'cam', ip='0'),
        View('addDevice', 'addDev'),
        View('addCond', 'addCon'),
        View('addSmall', 'addSmall'),
        View('addEffect', 'addEffect'),

    )



nav.init_app(app)


app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config.from_object(Config)
Bootstrap(app)
from app import hello
