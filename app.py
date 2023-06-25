from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def main():
    return render_template('main.html')

@app.route('/dashboard')
def display_dash():
    title = 'Dashboard'
    return render_template('dashboard.html', title=title)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)