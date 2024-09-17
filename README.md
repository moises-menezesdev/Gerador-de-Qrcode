# Gerador-de-Qrcode
Automatically generate QR codes in Python in conjunction with an Excel spreadsheet

QR Code Generator from Excel Data
This Python project automates the creation of QR codes for each person listed in an Excel spreadsheet, generating QR codes containing the name, CPF, and leadership data. Each QR code is saved as a .png image in a local directory.

Prerequisites
Before running this project, you'll need to have installed:

Python 3.x
Required libraries:
pandas
qrcode
Pillow (for image handling)
You can install the required dependencies by running:
pip install pandas qrcode[pil]


Project Structure
qr_codes: Folder where the generated QR codes will be saved.
gerar_qrcodes.py: Main script that reads data from the Excel spreadsheet and generates the QR codes.
How to Use
Prepare the Excel Spreadsheet: Make sure your Excel spreadsheet contains the columns NOME (Name), CPF, and LIDERANÇA (Leadership), as these will be the data used in the QR code.

Run the Script:

Place the Excel file in the same directory as the gerar_qrcodes.py script.
In the terminal, run the following command to execute the script:
python gerar_qrcodes.py

Output:
The script will create a folder called qrcodes (if it doesn't already exist) and will save the QR code images for each person in the spreadsheet.
The files will be named in the format: NAME_qrcode.png, where NAME is the person's name from the spreadsheet.


Features
Excel Reading: Uses the pandas library to load data from the spreadsheet.
QR Code Generation: The qrcode library is used to create QR codes based on the provided data (name, CPF, leadership).
Directory Creation: The code creates a qrcodes folder to store the QR code images, if it doesn't exist already.
Potential Improvements
Add validation to prevent generating QR codes for incomplete data.
Add support for additional columns of data in the QR code.
Create a graphical user interface (GUI) to make it easier for non-technical users to interact with the script.
Contributions
Feel free to contribute with improvements, bug reports, or suggestions. You can open a pull request or an issue to discuss any changes.

