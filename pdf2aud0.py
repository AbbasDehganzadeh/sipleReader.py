# importing the modules
import PyPDF2
import pyttsx3

# path, and pages of the PDF file
path = 'nodejs.pdf'
pdf = open(path, "rb")

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfReader(pdf)

# the page with which you want to start
# breakpoint()
from_page = pdfReader.pages[1]
# extracting the text from the PDF
text = from_page.extract_text()

# reading the text
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()

