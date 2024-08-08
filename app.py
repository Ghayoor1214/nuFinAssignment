import os
from flask import Flask, request, render_template, redirect, url_for, send_file
import pandas as pd
from prettytable import PrettyTable

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'


@app.route('/')
def index():
    """Render the file upload form."""
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and save it to the server."""
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        return redirect(url_for('process_file', filename=file.filename))


@app.route('/process/<filename>')
def process_file(filename):
    """Process the uploaded file and calculate required columns."""
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    if file_path.endswith('.csv'):
        data = pd.read_csv(file_path)
    else:
        data = pd.read_excel(file_path)

    # Ensure 'Input' column is numeric
    data['Input'] = pd.to_numeric(data['Input'], errors='coerce')

    # Calculation logic
    data['Change'] = data['Input'].diff()
    data['Gain'] = data['Change'].apply(lambda x: x if x > 0 else 0)
    data['Loss'] = data['Change'].apply(lambda x: -x if x < 0 else 0)
    data['Avg Gain'] = data['Gain'].rolling(window=14).mean()
    data['Avg Loss'] = data['Loss'].rolling(window=14).mean()
    data['HM'] = data['Avg Gain'] / data['Avg Loss']
    data['HMA'] = data['Input'].rolling(window=14).mean()

    output_file = os.path.join(app.config['UPLOAD_FOLDER'], 'processed_' + filename)
    data.to_csv(output_file, index=False)

    # Create PrettyTable
    table = PrettyTable()
    table.field_names = data.columns.tolist()
    for row in data.itertuples(index=False):
        table.add_row(row)

    table_html = table.get_html_string()

    return render_template('result.html', table=table_html, download_link=output_file)


@app.route('/download/<filename>')
def download_file(filename):
    """Provide file download."""
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(file_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
