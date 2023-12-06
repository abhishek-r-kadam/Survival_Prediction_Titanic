from flask import Flask,request,render_template
from project_data.utils import TitanicPrediction
import config

app = Flask(__name__)

@app.route("/")
def home_api():
    return render_template("index.html")

@app.route("/predict",methods = ["post"])
def prediction():
    
    data = request.form
    
    Pclass = eval(data["Pclass"])
    Sex = data["Sex"]
    Age = eval(data["Age"])
    SibSp = eval(data["SibSp"])
    Parch = eval(data["Parch"])
    Fare = eval(data["Fare"])
    Embarked = data["Embarked"]
    
    obj = TitanicPrediction(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked)
    
    prediction = obj.predict()
    
    if prediction == 1:
        return render_template("survived_template.html")
    elif prediction == 0:
        return render_template("died_template.html")
    else:
        # Handle other cases or errors as needed
        return "Unknown prediction result"

app.run(debug = True,host='0.0.0.0')