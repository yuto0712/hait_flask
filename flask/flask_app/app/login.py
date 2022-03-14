from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        print(f'POSTされたIDは{request.form["id"]}です')
        print(f'POSTされたPASSは{request.form["password"]}です')
        return render_template('form.html', message='登録しました')
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(port=8000, debug=True)