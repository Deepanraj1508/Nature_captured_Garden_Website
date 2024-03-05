from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(255), nullable=False)

# Ensure tables are created before running the app
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        customer_name = request.form.get('customerName')
        phone_number = request.form.get('phoneNumber')
        product_name = request.form.get('productName')
        quantity = request.form.get('quantity')
        address = request.form.get('address')

        # Get the current date and time
        order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create a dictionary with the form data and order date
        form_data = {
            'orderDate': order_date,
            'customerName': customer_name,
            'phoneNumber': phone_number,
            'productName': product_name,
            'quantity': quantity,
            'address': address,
        }

        # Read existing data from the JSON file, if any
        try:
            with open('Customer_data.json', 'r') as file:
                existing_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_data = []

        # Append the new data to the existing data
        existing_data.append(form_data)

        # Save the combined data back to the JSON file
        with open('Customer_data.json', 'w') as file:
            json.dump(existing_data, file, indent=2)

        # Redirect to the confirmation page
        return redirect(url_for('confirmation'))

    return render_template('index.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')



if __name__ == '__main__':
    app.run(debug=True , port=5001)
