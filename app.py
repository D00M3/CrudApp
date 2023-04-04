from flask import Flask
from flask import Flask,render_template,request,redirect
from models import db, FighterModel
from flask import abort


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
        fighters = FighterModel(Figher_id=Fighter_id, name=name, video_game=video_game, console=console)
        db.session.add(fighters)
        db.session.commit()
        return redirect('/data')
    
    """retrieve code"""
   
   
@app.route('/data')
def RetrieveDataList():
    fighters = FighterModel.query.all()
    return render_template('datalist.html', fighters = fighters)

@app.route('/data/<int:id>')
def RetrieveSingleEmployee(id):
    fighter = FighterModel.query.filter_by(Fighter_id=id).first()
    if fighter:
        return render_template('data.html', fighter = fighter)
    return f"Figher with id ={id} Doenst exist"

"Update Code"

@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    employee = FighterModel.query.filter_by(Fighter_id=id).first()
    if request.method == 'POST':
        if fighter:
            db.session.delete(fighter)
            db.session.commit()
 
            name = request.form['name']
            video_game = request.form['video_game']
            console = request.form['console']
            fighter = FighterModel(Fighter_id=id, name=name, video_game=video_game, console= console)
 
            db.session.add(fighter)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"Fighter with id = {id} Does nit exist"
 
    return render_template('update.html', fighter = fighter)

"delete code"

@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    fighter = FighterModel.query.filter_by(Fighter_id=id).first()
    if request.method == 'POST':
        if fighter:
            db.session.delete(fighter)
            db.session.commit()
            return redirect('/data')
        abort(404)
 
    return render_template('delete.html')
 
app.run(host='localhost', port=5000)