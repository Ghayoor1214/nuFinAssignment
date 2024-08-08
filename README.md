# Flask Application

This is a Flask application designed to process an Excel file and calculate values for specific columns based on the provided formulas. The results are then exported as a CSV file.

## Requirements

- Python 3.6+
- Flask
- pandas
- openpyxl

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/Ghayoor1214/nuFinAssignment.git)
   cd nuFinAssignment
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv env

3. **Activate the Virtual Environment**

   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Flask Application**

   ```bash
   flask run

   The application will be available at `http://127.0.0.1:5000/`.

## Usage

1. **Upload the Excel File**

   Navigate to `http://127.0.0.1:5000/upload` and upload the `hma.xls` file.

2. **Processing the File**

   The application will read the input from Column C, calculate the values for columns D, E, F, G, H, I, J based on the provided formulas, and export a CSV file with the calculated columns.

## Additional Information

- Ensure that your Excel file is named `hma.xls` and has the correct format as expected by the application.
- The `.gitignore` file is set up to exclude unnecessary files such as the virtual environment and temporary files.

