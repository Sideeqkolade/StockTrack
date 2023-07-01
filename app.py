from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def main():
    return render_template('main.html')

@app.route('/reports')
def display_report():
    title = 'Reports'
    return render_template('reports.html', title=title)

@app.route('/items')
def display_items():
    title = 'Items'
    return render_template('items.html', title=title)

@app.route('/inventory')
def display_inventory():
    title = 'Inventory'
    return render_template('inventory.html', title=title)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)