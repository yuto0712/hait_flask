from flask import Flask, jsonify

app = Flask(__name__, static_folder='.', static_url_path='')


@app.route('/mypage')
def mypage():
    login = True
    if login is False:
        return jsonify({
            'code': 400,
            'message': 'Bad Request'
            })
    user_data = {'user_name': 'ai_academy'}
    return jsonify({
        'code': 200,
        'message': 'OK',
        'result': user_data
    })


if __name__ == '__main__':
    app.run(port=8000, debug=True)
