# ItCanExtract - Simple OCR Tool

ItCanExtract is a beginner-friendly Win64 offline OCR tool that extracts text from images using Tesseract.

---

## Features

* Extracts text from PNG, JPG, JPEG images
* Saves output automatically to `output.txt` file
* Simple command-line interface
* Beginner-friendly execution using batch file

---

## Limitations

* Not 100% accurate
* Image quality affects results
* Code indentation may not be preserved
* Not suitable for handwritten text

---

## Download dependencies

1. Download Python: https://www.python.org/downloads/windows/
2. Download tesseract-ocr for Win64 (tesseract-ocr-w64-setup-5.5.0.20241111.exe): https://github.com/UB-Mannheim/tesseract/wiki

---

## Installation

1. Install Python 

2. Install tesseract-ocr: pip install pytesseract opencv-python
	![Install Tesseract](images/install_tesseract.png)
	
2.1. Set Tesseract-OCR install location's destination folder to: 
	"C:\Program Files\Tesseract-OCR\tesseract.exe"
	![Set PATH](images/set_tesseract_install_location.png)

---

## Usage

How To Use ItCanExtract:

Option 1: Double click run.bat (automated)

Then enter the image filename when prompted.


Option 2: Run itcanextract.py script in the cmd using the command:

python itcanextract.py

Then enter the image filename (e.g. image.png).
![Usage](images/usage_option2.png)


---Extracted Output---
![Usage](images/image2_extracted_output.png)

---

## Disclaimer

This tool is intended for general-purpose text extraction from images using optical character recognition (OCR) techniques.

While efforts have been made to ensure reliable functionality, OCR results may vary depending on factors such as image quality, resolution, formatting, and content complexity. As such, extracted text should be reviewed and validated before being used in any critical, legal, or decision-making context.

This software is provided for educational and productivity purposes only. The author makes no guarantees regarding accuracy, completeness, or fitness for a particular purpose, and assumes no liability for any direct or indirect consequences arising from its use.

Users are responsible for ensuring that their use of this tool complies with applicable laws, regulations, and organizational policies.


---

## Credits

* Tesseract OCR
* OpenCV

---

## AI Acknowledgment

This tool was developed with the assistance of ChatGPT.
