#Database Models
from flask_sqlalchemy  import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__='users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default = db.func.current_timestamp())
    
  
    
    def __init__(self,username,email,password_hash):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        
    
class Files(db.Model):
    __tablename__ = 'files'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    file_name = db.Column(db.String,nullable=False)
    file_path = db.Column(db.String, nullable=False)
    uploaded_at = db.Column(db.DateTime, default = db.func.current_timestamp())
    
    user = db.relationship('User', backref=db.backref('files', lazy=True))
    
    def __init__(self,user_id,file_name,file_path):
        self.user_id = user_id
        self.file_name = file_name
        self.file_path = file_path
    
class DataInsights(db.Model):
    __tablename__ = 'data_insights'
    
    id = db.Column(db.Integer, primary_key=True)
    file_id = db.Column(db.Integer, db.ForeignKey('file.id'), nullable=False)
    insights_type = db.Column(db.String(80), nullable=True)
    insights_data = db.Column(db.String(80), nullable=True)
    created_at = db.Column(db.DateTime, default = db.func.current_timestamp())
    
    file = db.relationship('Files', backref=db.backref('insights', lazy=True))
    
    def __init__(self,file_id,insights_type,insight_data):
        self.file_id = file_id
        self.insights_type = insights_type
        self.insights_data = insight_data
    
class VisualizationConfig(db.Model):
    __tablename__ = 'visualization_config'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    chart_type = db.Column(db.String(50), nullable=False)
    config_data = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, default = db.func.current_timestamp())
    
    user = db.relationship('User', backref=db.backref('visualization', lazy=True))
    
    def __init__(self,user_id,chart_type,config_data):
        self.user_id = user_id
        self.chart_type = chart_type
        self.config_data = config_data
    
    
