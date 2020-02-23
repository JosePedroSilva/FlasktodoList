from datetime import datetime
from app import db


class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<Note: {self.content}>'

    def delete_note(self, note):
        n = Note.query.filter_by(id=note)
        db.session.delete(n)
        db.session.commit()
    