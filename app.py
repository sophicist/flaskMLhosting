from flask import Flask, redirect, url_for, request,render_template
import pandas as pd
app = Flask(__name__)
 
 
from flask import Flask  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/', methods=['GET', 'POST'])
def main():
    
    # If a form is submitted
    if request.method == "POST":
        
        # Unpickle classifier
        #clf = joblib.load("clf.pkl")
        
        # Get values through input bars
        height = request.form.get("height")
        weight = request.form.get("weight")
        
        # Put inputs to dataframe
        X = pd.DataFrame([[height, weight]], columns = ["Height", "Weight"])
        
        # Get prediction
        # prediction = clf.predict(X)[0]
        prediction = f"{height} {weight}"
        
    else:
        prediction = ""
        
    return render_template("website.html", output = prediction)

 
if __name__ == '__main__':
    app.run(debug=True)