from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/attrazioni')
def attrazioni():
    return render_template('attrazioni.html')

@app.route('/eventi')
def eventi():
    return render_template('eventi.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5840, debug=True)