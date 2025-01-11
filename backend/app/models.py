#Database Models
from flask_sqlalchemy  import SQLAlchemy

db = SQLAlchemy()

class ExampleModel(db.Model):
    id = db.column(db.Integer, primary_key = True)
    name = db.column(db.String(80), nullable = False)
    
    
