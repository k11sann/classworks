import os
import openpyxl
from docxtpl import DocxTemplate

output_folder = os.path.dirname(os.path.abspath(__file__))   
wb = openpyxl.load_workbook(f'{output_folder}\\test.xlsx')
ws = wb.active
data = []
for row in ws.iter_rows(min_row=2):
    data.append({
        'name': row[0].value,
        'reason': row[1].value,
        'chill_time': row[2].value
    })

print(data)
template = DocxTemplate(f'{output_folder}\\shablon.docx')
for i, record in enumerate(data):
    template.render(record)
    filename = f'{output_folder}/results/result_{i + 1}.docx'
    template.save(filename)