# import necessary libraries
import os
# import prediction
import psycopg2
# from sklearn 
import joblib
import pickle
import numpy as np
import pandas as pd
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

IMAGE_FOLDER =os.path.join('static', 'images')

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config['UPLOAD_FOLDER']=IMAGE_FOLDER

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('final-project.cbgqvzvry5u3.us-east-2.rds.amazonaws.com', '') 
# or "sqlite:///db.sqlite"

# # Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# from .models import Pet


# create route that renders index.html template
@app.route("/")
@app.route("/index.html")
def home():
    full_filename=os.path.join(app.config['UPLOAD_FOLDER'], '4_weeks.jpg')
    return render_template("index.html", user_image=full_filename)

# create route that renders bio_page.html template
@app.route("/bio_page.html")
def bio_page():
    return render_template("bio_page.html")

# create route that renders project_summary.html template
@app.route("/project_summary.html")
def project_summary():
    return render_template("project_summary.html")

# create route that renders fetal_health_predictor.html template
@app.route("/fetal_health_predictor.html")
def fetal_health_predictor():
    return render_template("fetal_health_predictor.html")

# clf = load('finalized_model.sav')
@app.route('/predict', methods=['POST'])
def predict():
     # try out for code on Heroku
    clf = pickle.load(open('finalized_model.sav', 'rb'))
    print('clf')
    int_features = [float(x) for x in request.form.values()]
    query_df = [np.array(int_features)]
    print(query_df)
    # query = pd.get_dummies(query_df)

    # for col in model_columns:
    #     if col not in query.columns:
    #         query[col] = 0

    prediction = clf.predict(query_df)
    print(prediction)
    prediction_dictionary = {
        1: "The health of the fetus is likely normal.",
        2: "The health of the fetus is suspicious for possible pathology.",
        3: "The health of the fetus is likely pathological."
    }
    if int(prediction) in prediction_dictionary.keys():
        prediction_string=prediction_dictionary[int(prediction)]
    return render_template('fetal_health_predictor.html', prediction = prediction_string)

# @app.route('/results',methods=['POST'])
# def results():
#     data = request.get_json(force=True)
#     prediction = clf.predict(np.array[query])
#     output = prediction
#     return jsonify(output)

if __name__ == "__main__":
    clf = pickle.load(open('finalized_model.sav', 'rb'))
    app.run(debug=True)
