from flask import Flask, render_template, request
from database.db import insert_purchase  # Import the insert function from db.py

app = Flask(__name__)

@app.route('/purchase_form')
def purchase_form():
    return render_template("purchase_form.html")

@app.route('/submit_purchase', methods=["POST"])
def submit_purchase():
    data = request.form
    purchase_date = data['purchase_date']
    category = data['category']
    amount = data['amount']

    # Call the insert_purchase function from db.py
    success = insert_purchase(purchase_date, category, amount)

    if success:
        return f"Compra registrada con éxito: Fecha: {purchase_date}, Categoría: {category}, Monto: ${amount} COP"
    else:
        return "Error al registrar la compra."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

