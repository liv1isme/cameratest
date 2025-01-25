import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # Render the home page with a QR code scanner
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan_qr_code():
    # Handle the scanned QR code data
    qr_data = request.form.get('qr_data')
    if not qr_data:
        return "No QR code data received!", 400
    
    # You can add any logic here to handle the QR code data (e.g., redirecting, saving, etc.)
    return render_template('success.html', qr_data=qr_data)

if __name__ == '__main__':
    app.run(debug=True)
