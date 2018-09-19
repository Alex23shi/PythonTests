import openpyxl
from openpyxl import workbook, load_workbook

wb = load_workbook(filename= r'Sparkling Market Snapshot Report_JUN18.xlsx')
sheet = wb['RawData']
#b4 = sheet['B4']
#print(f'({b4.column}, {b4.row}) is {b4.value}')
manu = input("Input manufacturer: KO/PCI")
if manu == "KO":
    manufacturer = "Total TCCC"
else:
    manufacturer = "Total Pepsico"
fact = input("Input Fact: Value/Volume")

