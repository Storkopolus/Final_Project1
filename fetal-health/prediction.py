from flask import Flask, jsonify
from sklearn.externals import joblib
import pandas as pd 

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    json = request.json
    query_df = pd.DataFrame(json_)
    query = pd.get_dummies(query_df)

    # for col in model_columns:
    #     if col not in query.columns:
    #         query[col] = 0

    predicition = clf.predict(query)
    return jsonify({'prediction': list(predicition)})

if __name__ == '__main__':
    clf = joblib.load('finalized_model.sav')
    # model_columns = joblib.load('finalized_model.sav')
    app.run(port=8080)