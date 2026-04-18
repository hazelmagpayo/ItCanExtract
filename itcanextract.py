import pytesseract
import cv2
import os

# Path to Tesseract
# "r" before path means raw string
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(image_path):
    img = cv2.imread(image_path)

    if img is None:
        return None

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)
    return text


def main():
    # Ask user for filename
    image_name = input("Enter image filename (e.g. image.png): ").strip()

    # Resolve path relative to script folder
    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(base_dir, image_name)

    output_file = os.path.join(base_dir, "output.txt")

    print("\nProcessing...\n")

    text = extract_text(image_path)

    if text is None:
        print("ERROR: Image not found or unreadable.")
        input("Press Enter to exit...")
        return

    # KEEP YOUR WORKING OUTPUT LOGIC (UNCHANGED STYLE)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    print("Saved to output.txt")
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()