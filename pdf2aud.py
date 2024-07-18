# importing the modules
import os
from pathlib import Path
import sys

# 3rd modules
import PyPDF2
import pyttsx3

# path, and pages of the PDF file
path = sys.argv[1]
pages = sys.argv[2]
# TODO supports `_`, `-` for multiple ranges
first, last = pages, pages
if pages.count(":"):
    first, last = pages.split(":")
if not (first.isnumeric() and last.isnumeric()):
    raise TypeError(f"argument pages must be integer, got {first, last}")
first, last = int(first), int(last)

path = Path(os.getcwd(), path)  # full path
pdf = open(path, "rb")

# creating a PdfFileReader, and speaker object
pdfReader = PyPDF2.PdfReader(pdf)
speak = pyttsx3.init()

# the page with which you want to start
# breakpoint()
for page in range(first - 1, last):  # page adjustment
    from_page = pdfReader.pages[page]
    # extracting the text from the PDF
    text = from_page.extract_text()

    # reading the text
    speak.say(text)
speak.runAndWait()
