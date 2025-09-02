import os
from docx2pdf import convert
from PyPDF2 import PdfReader, PdfWriter
from pdf2docx import Converter

# Define directories
input_dir = "/Users/john/Downloads/test-dir"
output_dir = "/Users/john/Downloads//COPY"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Get all .docx files in the input directory
docx_files = [f for f in os.listdir(input_dir) if f.endswith('.docx')]

# for loop for each file in docx_files
for docx_file in docx_files:
    input_docx = os.path.join(input_dir, docx_file)
    temp_pdf = os.path.join(input_dir, f"temp_{docx_file.replace('.docx', '.pdf')}")
    modified_pdf = os.path.join(input_dir, f"v_{docx_file.replace('.docx', '.pdf')}")
    output_docx = os.path.join(output_dir, f"v_{docx_file}")

    # Step 1: Convert Word to PDF
    convert(input_docx, temp_pdf)

    # Step 2: Remove the first page from the PDF
    pdf_reader = PdfReader(temp_pdf)
    pdf_writer = PdfWriter()

    # Check if the PDF has at least one page
    if len(pdf_reader.pages) > 0:
        # Copy all pages except the first one
        for page_num in range(1, len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        # Save the modified PDF
        with open(modified_pdf, 'wb') as f:
            pdf_writer.write(f)

        # Step 3: Convert the modified PDF back to Word
        cv = Converter(modified_pdf)
        cv.convert(output_docx, start=0, end=None)
        cv.close()

        # Clean up temp PDF files
        os.remove(temp_pdf)
        os.remove(modified_pdf)

        # print(f"Processed {docx_file}, output saved to {output_docx}")
    else:
        # print(f"Skipped {docx_file}: PDF has no pages or is invalid.")
        # Clean up temporary PDF file if it exists
        if os.path.exists(temp_pdf):
            os.remove(temp_pdf)

print("Files processed and placed in: " + output_dir)