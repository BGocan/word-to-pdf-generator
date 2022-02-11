from locale import currency
from docx2pdf import convert
import os
import glob

current_dir = os.getcwd() # gets current directory

# Source Directory (the docx files)

path = os.listdir(current_dir)

for i,files in enumerate(path):
    if files[-5:] == ".docx":
        convert(".//"+f"{files}",  ".//" + f"Book{i}.pdf")