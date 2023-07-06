import database
import csv
from flask import Flask, render_template, request, make_response, redirect
from database import add_data_db, show_items, show_purchase_report, create_csv_string
app = Flask(__name__)

@app.route('/')
@app.route('/home', strict_slashes=False)
def main():
    return render_template('main.html')

@app.route('/reports', strict_slashes=False)
def display_report():
    title = 'Reports'
    return render_template('reports.html', title=title)


@app.route('/inventory', methods=['GET', 'POST'], strict_slashes=False)
def display_inventory():
    title = 'Inventory'
    if request.method == 'POST':
        # Process the form data and save it to the database
        data = request.form
        print(data)
        add_data_db(data)
        print('Form submitted successfully')
        # Redirect back to the same page (GET request)
        return redirect('/inventory')

    # Display the inventory form
    return render_template('inventory.html', title=title)

@app.route('/items', strict_slashes=False)
def display_items():
    """extracting items from database"""

    title = 'Items'
    
    # Getting the return of the function in result
    result = show_items()

    # Rendering the result 
    return render_template('items.html', title=title, result=result)


@app.route('/purchase_report', strict_slashes=False)
def display_purchase():
    """function that renders the purchase report"""
    
    title = 'Purchase Report'

    # Getting the report fron database
    purchase_report = show_purchase_report()
    
    # Rendering the template
    return render_template('purchase_report.html', title=title, purchase_report=purchase_report)

@app.route('/download_purchase_report', strict_slashes=False)
def download_purchase_report():
    """function that downloads the csv file of purchase_report"""

    report_data = show_purchase_report()
    csv_data = create_csv_string(report_data)
    response = make_response(csv_data)

    response.headers['Content-Disposition'] = 'attachment; filename=purchase_report.csv'
    response.headers['Content-Type'] = 'text/csv'

    return response
    




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)