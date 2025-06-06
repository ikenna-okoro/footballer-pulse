from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FansComment(db.Model):
    __tablename__ = 'fans_comments'
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'team_name': self.team_name,
            'username': self.username,
            'comment': self.comment
        }
