from openpyxl import Workbook
from openpyxl.styles import Font
import time

book = Workbook()
sheet = book.active

sheet['A1'] = 'IP'


sheet['A1'].font = Font(bold=True)

sheet['B1'] = 'ACCESS DATE'
sheet['B1'].font = Font(bold=True)

sheet['C1'] = 'ACCESS TIME'
sheet['C1'].font = Font(bold=True)

sheet['D1'] = 'METHOD'
sheet['D1'].font = Font(bold=True)

sheet['E1'] = 'URL'
sheet['E1'].font = Font(bold=True)

sheet['F1'] = 'OPERATIVE SYSTEM'
sheet['F1'].font = Font(bold=True)

for i in range(2, 15):
    sheet[f'B{i}'] = i

book.save('Access Log Cleaned.xlsx')

