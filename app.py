from flask import Flask
from flask import Flask,render_template,request,redirect
from models import db,FighterModel
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///<FightersDB>.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()

""" This is the create code of the App"""

@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        Fighter_id = request.form['Fighter_id']
        name = request.form['name']
        video_game = request.form['video_game']
        console = request.form['console']
        fighter = FighterModel(Figher_id=Fighter_id, name=name, video_game=video_game, console=console)
        db.session.add(fighter)
        db.session.commit()
        return redirect('/data')
 
app.run(host='localhost', port=5000)