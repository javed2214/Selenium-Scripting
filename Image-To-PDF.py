# Image to PDF Converter

import img2pdf 
from PIL import Image 
import os 
  
img_path = "C:/Image.jpg"       # Image Path  
  
pdf_path = "C:/PDF_File.pdf"    # PDF File Path
  
image = Image.open(img_path) 
  
pdf_bytes = img2pdf.convert(image.filename) 
  
file = open(pdf_path, "wb") 
  
file.write(pdf_bytes) 
  
image.close() 
  
file.close() 
  
print("Successfully Converted into PDF!!!") 
