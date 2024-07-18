# importing the modules
import os
from pathlib import Path
import sys

# 3rd modules
import PyPDF2
import pyttsx3

def parse_input(path, pages):
    ranges = pages.split('-') # for indicating range of pages
    pages= []
    for t in ranges:
        # TODO: regard the case `:n`, `n:`
        if t == '': # im case -gt `-`
            continue
        page=t.split(':')
        if len(page) == 1:#one page
            page.append(page[0])
        elif len(page) > 2:
            raise SyntaxError("there must be one `:` in page argument")
        pages.append(page)            
    pages = [list(map(int,page)) for page in pages]

    path = Path(os.getcwd(),path) # full path

    return path, pages

def pdf_speak(pdfReader, first, last):
    breakpoint()
    for page in range(first-1,last): # page adjustment
        from_page = pdfReader.pages[page]
        # extracting the text from the PDF
        text = from_page.extract_text()
        if text != '': #NOTICE: check to prevent speak error
            speak.say(text)
    
    # reading the text
    speak.runAndWait()

# path, and pages of the PDF file
path = sys.argv[1]
pages=sys.argv[2]
file, pages = parse_input(path, pages)
pdf = open(file, "rb")

# creating a PdfFileReader, and speaker object
pdfReader = PyPDF2.PdfReader(pdf)
speak = pyttsx3.init()

# the page with which you want to start
for page in pages:
    pdf_speak(pdfReader, page[0], page[1])
