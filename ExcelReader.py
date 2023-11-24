#!/usr/bin/env python

# pip install pandas openpyxl

import pandas as pd

def read_emails_from_excel(file_path, sheet_name, email_column_index):
    # Read the Excel sheet into a DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
    
    # Extract the emails from the specified column index
    emails = df.iloc[:, email_column_index].tolist()
    
    return emails

# Example usage
file_path = '/home/gns3/PostgresLibpq/EmailParser.xlsx'  # Replace with the actual file path
sheet_name = 'Sheet1'  # Replace with the actual sheet name
email_column_index = 1  # Assuming the email column is the second column (index 1)

emails = read_emails_from_excel(file_path, sheet_name, email_column_index)
for email in emails:
        print ("INSERT INTO students (name, email, is_jackpot, enrollment_date, price_paid, ph_no) VALUES ('" + email + "', '" + email + " ', false, '2023-07-01', 0, '-');")

# once emails.txt is created, run below cmd to import all emails in DB
# psql -U postgres -h localhost -d postgres -f emails.txt
