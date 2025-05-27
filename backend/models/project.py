# backend/models/project.py
from app import db

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'url': self.url
        }


