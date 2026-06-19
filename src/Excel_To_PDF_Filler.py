
"""
PDF Automation Toolkit

A collection of Python tools for PDF workflow automation.

Created by ipvl
"""


#import pip modules

import openpyxl
from pypdf import PdfReader, PdfWriter
import os
import sys
import json

#defining the variables as sys arguments

if len(sys.argv) != 4:
    print("Please enter: python(os equivalent) Excel_To_PDF_Filler.py excel.xlsx template.pdf output_folder")
    sys.exit(1)

excel_file = sys.argv[1]
template_pdf = sys.argv[2]
output_folder = sys.argv[3]

#create a folder for the output (output_folder), if it already exists, don't throw an error

os.makedirs(output_folder, exist_ok=True)

#load the config.json file

with open("config.json") as file:
    config = json.load(file)

#load the excel document into python; select the sheet

workbook = openpyxl.load_workbook(excel_file)
sheet = workbook.active

#defining a 2.d.p funtion (for currency)

def to_2dp(value):
    try:
        return f"{round(float(value), 2):.2f}"
    except (TypeError, ValueError):
        return value

#core loop

for index, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):

    data = list(row)

    fields = {}

    for pdf_field, excel_position in config["fields"].items():
        fields[pdf_field] = row[excel_position]

    reader = PdfReader(template_pdf)
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)


    writer.update_page_form_field_values(
        writer.pages[0], 
        fields
    )

    output = os.path.join(output_folder, f"{data[0]}.pdf") #change {data[0]} if you want the outputs to be called something else

    with open(output, "wb") as file:
        writer.write(file)

print(f"Completed with config: {config['fields']}") #confirming script ran successfully
