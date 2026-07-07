from pdf2image import convert_from_bytes
import easyocr
import numpy as np

reader = easyocr.Reader(['en'])

def extract_text_from_scanned_pdf(uploaded_file):

    print("STEP 1: OCR function started")

    uploaded_file.seek(0)

    pdf_bytes = uploaded_file.read()

    print("STEP 2: PDF bytes read")

    images = convert_from_bytes(
        pdf_bytes,
        poppler_path=r"C:\poppler\poppler-26.02.0\Library\bin"
    )

    print(f"STEP 3: Converted {len(images)} pages")

    full_text = ""

    for i, image in enumerate(images):

        print(f"Reading page {i+1}")

        image_np = np.array(image)

        result = reader.readtext(
            image_np,
            detail=0
        )

        full_text += "\n".join(result)
        full_text += "\n"

    print("STEP 4: OCR completed")

    return full_text