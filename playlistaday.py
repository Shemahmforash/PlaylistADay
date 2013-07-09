from flask import Flask, render_template, jsonify, json
import urllib
app = Flask(__name__)

@app.route('/')
@app.route('/<path:date>')
def main(date=None):
    return render_template('base.html', date=date)

@app.route('/getplaylist/')
@app.route('/getplaylist/<date>')
def events(date=None):
    #TODO: change json events source
    data = json.load(urllib.urlopen('http://wanderer-red-laptop/dayinmusic/examples/'))

    #TODO: parse event data and find the artist associated with each description (using echonest)

    #TODO: generate a playlist using the data found

    return jsonify( data )

if __name__ == '__main__':
    app.debug = True
    app.run()
