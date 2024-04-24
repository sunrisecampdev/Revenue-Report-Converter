# NetSuite Revenue Report Converter
Basic python script to convert the shitty NetSuite reports to something we can actually use.

# Requirements
Python 3.12.3+
Openpyxl 3.1.2

# How to Use:
Download the revenue report from NetSuite
Open Excel on desktop and create a new spreadsheet
Copy everything from the DEVRevenue report from NetSuite
Paste it into the new blank spreadsheet you just created
Save the new revenue report as newrev.xlsx

Move test.py and newrev.xlsx into the same folder
Double click on test.py

There should be a new .xlsx file called superReport
Open superReport - the new revenue report will appear under Sheet2
