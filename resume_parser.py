import pdfplumber
from docx import Document

from PIL import Image
import pytesseract
import cv2

# -----------------------------------
# TESSERACT PATH
# -----------------------------------

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# -----------------------------------
# EXTRACT TEXT
# -----------------------------------

def extract_text(file_path):

    text = ""

    # PDF
    if file_path.endswith(".pdf"):

        with pdfplumber.open(file_path) as pdf:

            for page in pdf.pages:

                extracted = page.extract_text()

                if extracted:
                    text += extracted

    # DOCX
    elif file_path.endswith(".docx"):

        doc = Document(file_path)

        for para in doc.paragraphs:

            text += para.text + "\n"

    # IMAGE
    elif (
        file_path.endswith(".jpg")
        or
        file_path.endswith(".jpeg")
        or
        file_path.endswith(".png")
    ):

        image = cv2.imread(file_path)

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        text = pytesseract.image_to_string(gray)

    return text