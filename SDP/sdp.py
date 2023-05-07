#Import packages
from flask import Flask, render_template,request
from pymongo import MongoClient

client = MongoClient('localhost',27017)
db=client['flask']
data=db.users

#creating an Instance (Flask)
app=Flask(__name__)
@app.route("/check", methods=['post', 'get'])
def check():

    email = request.form.get("email")
    psw = request.form.get("psw")
    pswrepeat=request.form.get("pswrepeat")
    db.agriaqua.insert_one({

        "email": email,
        "psw": psw,
        "pswrepeat":pswrepeat,
    })
    return render_template("home.html")
@app.route("/check1", methods=['post', 'get'])
def check1():

    mail = request.form.get("mail")
    name=request.form.get("name")
    db.agriaqua.insert_one({

        "mail": mail,
        "name":name
    })
    return render_template("home.html")

#Route/Rendering -Normal Route
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/Register")
def register():
    return render_template('Register.html')

@app.route("/availabilityofmachinesagr")
def availabilityofmachinesagr():
    return render_template('availabilityofmachinesagr.html')

@app.route("/availabilityofmachinesaqu")
def availabilityofmachinesaqu():
    return render_template('availabilityofmachinesaqu.html')

@app.route("/Login")
def Login():
    return render_template('Login.html')

@app.route("/informationaboutcrops")
def informationaboutcrops():
    return render_template('informationaboutcrops.html')

@app.route("/informationaboutaqualife")
def informationaboutaqualife():
    return render_template('informationaboutaqualife.html')

@app.route("/buynow")
def buynow():
    return render_template('buynow.html')

@app.route("/ContactUs")
def contact():
    return render_template('Contact.html')

@app.route("/fertilizers")
def fertilizers():
    return render_template('fertilizers.html')

@app.route("/AboutUs")
def aboutus():
    return render_template('aboutus.html')

@app.route("/seeds")
def seeds():
    return render_template('seeds.html')

@app.route("/addtocart")
def addtocart():
    return render_template('addtocart.html')

@app.route("/paynow")
def paynow():
    return render_template('paynow.html')

@app.route("/kharifseason")
def kharifseason():
    return render_template('kharifseason.html')

@app.route("/rabiseason")
def rabiseason():
    return render_template('rabiseason.html')

@app.route("/zaidseason")
def zaidseason():
    return render_template('zaidseason.html')

if __name__=="__main__":
    app.run();

