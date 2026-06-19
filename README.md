
A collection of automated pdf tools

## How to install

Python3 is needed for this script to run.
Python commands vary based on OS, this is Windows:

    py install
    py -m pip install pypdf openpyxl

    git clone https://github.com/IPvLgit/PDF-Automation-Toolkit.git

---

### 1. Excel To PDF Form Filler

Takes data from an Excel spreadsheet and fills PDF form fields, creating a new completed PDF for each row.
This tool is used if you need to copy data from excel rows into specific pdf template and specific form fields.

Features

- Reads data from Excel files
- Fills PDF form fields automatically
- Creates one PDF output per Excel row
- Uses a configurable JSON mapping
- Supports any number of PDF fields with unlimited output

How It Works

The script maps PDF form field to Excel column.
You configure the form fields in the 'config.json' file, replacing 'example' with the form field ID. You can add as many form fields as you want.
   
    Example:

    ```json
    {
     "fields": {
         "Name": 0,
          "Address": 1,
         "JobDescription": 2,
         "Salary": 3
        }
    }

    *if you dont know the form field IDs use my other tool 'PDF_Field_Checker'

Usage

python Excel_To_PDF_Filler.py excel.xlsx pdftemplate.pdf outputfoldername
    *if the output folder exists the pdfs will be sent there, if it doesnt exist the script will create one

---

### 2. PDF Field Reader

Extracts available form fields from a PDF.

Features:
- Lists all fillable PDF fields
- Used with the Excel to PDF Form Filler tool create config mappings

Usage:

python PDF_Field_Reader.py example.pdf

---

### 3. PDF Flattener

Takes a folder of PDFs and flattens them to remove form fields
This is important to merging PDFs into one while maintaining data integrity

Features:
- Takes the output folder from the filler tool and flattens all PDFs, outputing a new folder
- Used with the merger tool to merge PDFs without data being altered.

Usage:

python PDF_Flattener.py inputfolder outputfolder

---

### 4. PDF Merger

Takes a folder of PDFs and merges them into a single PDF
Used after the flattener to maintain data

Features:
- Can be used in conjunction with my other tools to create a workflow, quickly merging PDFs
- Works with the flattener to keep data across pages

Usage:

python PDF_Merger inputfoder output.pdf



Written by ipvl
