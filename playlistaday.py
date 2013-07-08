from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
@app.route('/<path:date>')
def main(date=None):
    return render_template('base.html', date=date)

@app.route('/getevents/')
@app.route('/getevents/<date>')
def events(date=None):
    return jsonify()

if __name__ == '__main__':
    app.debug = True
    app.run()
