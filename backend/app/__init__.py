from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRER KEY'] = '612dcce911c2879e19559c1cf2a2d1da5cf9620bc50bec7a'
    
    #blueprint and routes
    from .routes import main
    app.register_blueprint(main)
    
    return app