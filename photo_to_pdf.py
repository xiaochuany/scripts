"""convert photo to pdf"""

from PIL import Image
import os

def convert_jpg_to_pdf(image_path, output_path):
    # Open the image
    image = Image.open(image_path)
    # Ensure the image is in RGB mode
    if image.mode != 'RGB':
        image = image.convert('RGB')
    # Save the image as a PDF
    image.save(output_path, 'PDF')


# Get the current directory
current_directory = os.getcwd()

# Collect all JPG files in the current directory
jpg_files = [file for file in os.listdir(current_directory) if file.lower().endswith('.jpg')]

# Convert each JPG file to PDF
for jpg_file in jpg_files:
    # Construct the paths for the input JPG file and output PDF file
    jpg_path = os.path.join(current_directory, jpg_file)
    pdf_path = os.path.splitext(jpg_path)[0] + '.pdf'
    # Convert the JPG file to PDF
    convert_jpg_to_pdf(jpg_path, pdf_path)