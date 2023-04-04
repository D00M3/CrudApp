from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class Model_name(db.Model):
    __tablename__ = 'Fighters'
 
    id = db.Column(db.Integer, primary_key = True)
    Fighter_id = db.Column(db.Integer(),unique = True)
    name = db.Column(db.string())
    video_game = db.Column(db.string())
    console = db.coluum(db.string())
 
    def __init__(self,Fighter_id,name,video_game,console):
        self.Fighter_id = Fighter_id
        self.name = name
        self.video_game = video_game
        self.console = console
 
    def __repr__(self):
        return f"{self.Fighter_id}:{self.name}:{self.video_game}{self.console}"