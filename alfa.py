import flask

def create_app(logger_instance):
    app = Flask(__name__)
    app.config['LOGGER'] = logger_instance
    return app