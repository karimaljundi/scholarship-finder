from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Scholarship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), nullable=False)
    description = db.Column(db.Text, nullable=False)
    offered_by = db.Column(db.String(1000), nullable=False)
    type = db.Column(db.String(1000), nullable=False)
    citizenship_type = db.Column(db.String(1000), nullable=False)
    application_required = db.Column(db.String(1000), nullable=False)
    nature_of_award = db.Column(db.String(1000), nullable=False)
    application_deadline = db.Column(db.String(1000), nullable=False)
    value = db.Column(db.String(1000), nullable=False)
    university = db.Column(db.String(1000), nullable=False)
    

    def __init__(self, name, description, offered_by, type, citizenship_type, application_required, nature_of_award, application_deadline, value, university):
        self.name = name
        self.description = description
        self.offered_by = offered_by
        self.type = type
        self.citizenship_type = citizenship_type
        self.application_required = application_required
        self.nature_of_award = nature_of_award
        self.application_deadline = application_deadline
        self.value = value
        self.university = university
