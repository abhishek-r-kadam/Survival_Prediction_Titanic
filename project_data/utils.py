import pandas as pd
import numpy as np
import pickle
import json

import config



class TitanicPrediction():
    def __init__(self,Pclass, Sex, Age, SibSp, Parch, Fare,Embarked):
        self.Pclass = Pclass
        self.Sex = Sex
        self.Age = Age
        self.SibSp = SibSp
        self.Parch =Parch
        self.Fare = Fare
        self.Embarked = Embarked
        
    def load_model(self):
        
        with open(config.MODEL_PATH,"rb") as f:
            self.model = pickle.load(f) 
            
        # with open("input_data.json","r") as f:
        #     self.input_data = json.load(f)
            
    def predict(self):
        
        self.load_model()
        
        input_data = [self.Pclass,self.Sex,self.Age,self.SibSp,self.Parch,self.Fare,self.Embarked]
        
        result = self.model.predict([input_data])
        
        if result[0] == 1:
            return 1  # Survived
        else:
            return 0  # Died
    

if __name__ == "__main__":
        print("In main")
        Pclass = 3
        Sex = "male"
        Age = 30
        SibSp = 1
        Parch = 0
        Fare = 9
        Embarked = "S"
        
        model_p = TitanicPrediction(Pclass, Sex, Age, SibSp, Parch, Fare,Embarked)
        
        prediction = model_p.predict()
        
        print(prediction)
     
        