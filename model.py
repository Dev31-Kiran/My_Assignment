from flask import Flask, render_template, request, jsonify
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__, static_url_path='/static')


model = joblib.load('final_model.joblib')
transform_obj = joblib.load('final_tranformer.joblib')

@app.route('/', methods=['GET', 'POST'])
def land():
    prediction = None
    emoji = None

    if request.method == 'POST':
        user_input = request.form['user_input']
        preprocessed_input = transform_obj.transform([user_input])
        preprocessed_input = preprocessed_input.toarray()
        prediction = model.predict(preprocessed_input)[0]
        if prediction == 1:
            sentiment = 'POSITIVE'
            
        else:
            sentiment = 'NEGATIVE'
            

        return jsonify({"sentiment": sentiment, "Input": user_input})

    return render_template('land.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
