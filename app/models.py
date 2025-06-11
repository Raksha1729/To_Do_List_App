from app import db

class Task(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100),nullable=False) # cannot be empty
    status=db.Column(db.String(20),default="pending") # if user does not pick anything, then pending
