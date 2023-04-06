from flask_sqlalchemy import SQLAlchemy

db =SQLAlchemy()
 
class FighterModel(db.Model):
    __tablename__ = 'Fighter'
 
    id = db.Column(db.Integer, primary_key = True)
    fighter_id = db.Column(db.Integer(),unique = True)
    name = db.Column(db.String(15))
    video_game = db.Column(db.String(20))
    console = db.Column(db.String(10))
    
 
    def __init__(self,fighter_id,name,video_game,console):
        self.fighter_id = fighter_id
        self.name = name
        self.video_game = video_game
        self.console = console
 
    def __repr__(self):
        return f"{self.fighter_id}:{self.name}"