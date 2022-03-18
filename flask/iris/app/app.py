from flask import Flask, render_template, request
from wtforms import Form, FloatField, SubmitField, validators
import numpy as np
import joblib


def predict(paramaters):
    model = joblib.load('iris_model.pkl')
    params = paramaters.reshape(1, -1)
    pred = model.predict(params)
    return pred


def getName(label):
    print(label)
    if label == 0:
        return 'Iris Setosa'
    elif label == 1:
        return 'Iris Versicolor'
    elif label == 2:
        return 'Iris Virginica'
    else:
        return 'Error'


app = Flask(__name__)


class IrisForm(Form):
    SepalLength = FloatField('Sepal Length(cm) 萼の長さ',
                             [validators.InputRequired('この項目は入力必須です'),
                              validators.NumberRange(min=0,
                                                     max=10,
                                                     message='0~10以内で入力してください')
                              ])
    SepalWidth = FloatField('Sepal Width(cm) 萼の幅',
                            [validators.InputRequired('この項目は入力必須です'),
                             validators.NumberRange(min=0,
                                                    max=10,
                                                    message='0~10以内で入力してください')
                             ])
    PetalLength = FloatField('Petal Length(cm) 花弁の長さ',
                             [validators.InputRequired('この項目は入力必須です'),
                              validators.NumberRange(min=0,
                                                     max=10,
                                                     message='0~10以内で入力してください')
                              ])
    PetalWidth = FloatField('Petal Width(cm) 花弁の幅',
                            [validators.InputRequired('この項目は入力必須です'),
                             validators.NumberRange(min=0,
                                                    max=10,
                                                    message='0~10以内で入力してください')
                             ])

    submit = SubmitField('判定')


@app.route('/', methods=['GET', 'POST'])
def predicts():
    form = IrisForm(request.form)
    if request.method == 'POST' and form.validate():
        SepalLength = request.form['SepalLength']
        SepalWidth = request.form['SepalWidth']
        PetalLength = request.form['PetalLength']
        PetalWidth = request.form['PetalWidth']
        x = np.array([SepalLength, SepalWidth, PetalLength, PetalWidth])
        pred = predict(x)
        name = getName(pred)
        return render_template('result.html', irisName=name)
    elif request.method == 'GET':
        return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
