from flask import Flask, render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///root.db'

db=SQLAlchemy(app)

class User(db.Model):

  id=db.Column(db.Integer,primary_key=True)
  firstname= db.Column(db.String(100), nullable=False)
  lastname= db.Column(db.String(100), nullable=False)
  email= db.Column(db.String(100), nullable=False)
  message=db.Column(db.String(100), nullable=False)
  
  def __repr__(self):
    return '<Contact %r>' & self.id

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/contact',methods=['POST','GET'])

def contact():
  if request.method=='POST':
      email = request.form.get('email')
      firstname = request.form.get('firstname')
      lastname = request.form.get('lastname')
      message= request.message.form.get('message')
      new_contact = User(email=email,firstname=firstname,lastname=lastname,message=message)
  try:
      db.session.add(User)
      db.session.commit()
      return redirect('/')   
  except:
      return"Error adding new contact"

  else:
    
    return render_template('contact.html')


if __name__ == "__main__":
  app.run(debug=True)





   