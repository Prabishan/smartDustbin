from flask import *
import pyrebase

app = Flask(__name__)


firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
@app.route('/', methods=['GET','POST'])
def basic():
    if request.method =='POST':
        email = request.form['username']
        password = request.form['password']
        try:
            auth.sign_in_with_email_and_password(email,password)
            return redirect(url_for('dashboard'))
        except:
            return 'Unsuccessfull'
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    db = firebase.database()
   #user1 = {'weight':'500'}
    db_weight = db.child("weights").get().val().values()
    listWeight = list(db_weight)[0]
    totalWaste=0
    lisWeight = []
    for i in listWeight:
        totalWaste+=listWeight[i]
        lisWeight.append(listWeight[i])
    recentRecCol = lisWeight[-1]
    #percent = ((lisWeight[-1] - lisWeight[-2])/lisWeight[-2])*100
    #print(percent)
    #print(recentRecCol)
    return render_template('dashboard.html',trc=totalWaste,rrc=recentRecCol,array1 =listWeight)
if __name__ =='__main__':
    app.run()