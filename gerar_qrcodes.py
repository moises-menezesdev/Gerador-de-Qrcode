import pandas as pd
import qrcode
import os

# Step 1: Read the Excel file
df = pd.read_excel('your_spreadsheet_path.xlsx')  # Insert the path to your Excel file

# Step 2: Create a directory to save the QR codes, if it doesn't exist
if not os.path.exists('qrcodes'):
    os.makedirs('qrcodes')

# Step 3: Iterate over the spreadsheet rows and generate QR codes
for index, row in df.iterrows():
    name = row['NOME']
    cpf = row['CPF']
    leadership = row['LIDERANÇA']
    
    # Data to be stored in the QR code
    data = f"Name: {name}\nCPF: {cpf}\nLeadership: {leadership}"
    
    # Generate QR code
    img = qrcode.make(data)
    
    # Save the QR code as a PNG image
    img.save(f"qrcodes/{name}_qrcode.png")

print("QR codes generated successfully!")
