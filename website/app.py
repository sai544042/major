from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask import render_template,request,redirect
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView 

app = Flask(__name__)

db = SQLAlchemy(app)

admin = Admin(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hello.db'   #relative path
app.config['SECRET_KEY'] = 'mysecret'

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(30),unique = True)
   email = db.Column(db.String(80),unique = True)
   phone_num = db.Column(db.String(30),unique = True)
   branch = db.Column(db.String(30))
   password = db.Column(db.String(30))
   def __init__(self, username , email , password,phone_num,branch):
	    self.username = username
	    self.email = email
	    self.phone_num = phone_num
	    self.branch = branch
	    self.password = password

admin.add_view(ModelView(User,db.session))
			

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/signup",methods = ['GET','POST'])
def index1():
    if request.method == 'POST':
        username = request.values.get('username')
        email =  request.values.get('email') 
        password = request.values.get('password')
        branch = request.values.get('branch')
        phone_num = request.values.get('phone_num')
        new_user = User(username = username,email = email , password = password,branch = branch , phone_num = phone_num)
        db.session.add(new_user)
        db.session.commit()
        print(username)
        return redirect("/")
    return render_template("public/sign_up.html")

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/admin_template.html")

@app.route("/test")
def test():
    return render_template("index.html")
	
	
if __name__ == '__main__':
	app.run(debug = True)