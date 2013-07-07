from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<path:date>')
def main(date=None):
    return render_template('base.html', date=date)

if __name__ == '__main__':
    app.debug = True
    app.run()
