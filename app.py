from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/documents')
def documents():
    return render_template('documents.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')

@app.route('/system')
def system():
    return render_template('system.html')


if __name__ == '__main__':
    app.run(debug=True)