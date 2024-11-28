from PyPDF2 import PdfReader 

pdf_file_path = 'CategoryCodes.pdf'

with open(pdf_file_path, 'rb') as file:
    reader = PdfReader(file)
    
    num_pages = len(reader.pages)
    
    text = ""
    
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text += page.extract_text()
    
    print("Extracted Text: ")
    print(text)

with open("extracted.txt", "w", encoding="utf-8") as text_file:
    text_file.write(text)
