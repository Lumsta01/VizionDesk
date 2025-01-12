#Database Models
from flask_sqlalchemy  import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default = db.func.current_timestamp())
    
class Files(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'), nullable=False)
    file_name = db.Column(db.String,nullable=False)
    file_path = db.Column(db.String, nullable=False)
    uploaded_at = db.Column(db.DateTime, default = db.func.current_timestamp())
    
class DataInsights(db.Model):
    id = db.column(db.Integer, primary_key=True)
    file_id = db.column(db.Integer, db.ForeignKey('file_id'), nullable=False)
    insights_type = db.Column(db.String(80), nullable=True)
    insights_data = db.Column(db.String(80), nullable=True)
    created_at = db.Column(db.DateTime, default = db.func.current_timestamp())
    
    
