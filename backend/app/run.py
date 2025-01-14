from app import create_app
from models import db

app = create_app()

db.init_app(app)

with app.app_context():
    db.create_all

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000',debug=True)