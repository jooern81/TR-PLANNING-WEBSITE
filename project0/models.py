from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Consist(db.Model):
    __tablename__ = "Operations"
    id = db.Column(db.Integer, primary_key=True)
    #origin = db.Column(db.String, nullable=False)
    #destination = db.Column(db.String, nullable=False)
    consist_id = db.Column(db.String, nullable=False)

