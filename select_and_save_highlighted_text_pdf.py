import subprocess
import fitz
import tkinter as tk
from tkinter import filedialog

# Prompt user to select PDF file
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

# Open PDF file in new process
subprocess.Popen([file_path], shell=True)

# Prompt user to highlight text in the PDF file
print("Please highlight the text you want to save in a text file.")
print("Once you have finished highlighting, close the PDF viewer.")
input("Press 'Enter' to continue...")

# Capture highlighted text and save to text file
pdf_document = fitz.open(file_path)
text_file = open('highlighted_text.txt', 'w')
for page_num in range(pdf_document.page_count):
    page = pdf_document[page_num]
    annot = page.first_annot
    while annot:
        if annot.type[0] == 8:  # If the annotation is a rectangle
            text = page.get_text("text", clip=annot.rect).strip()
            if text:
                text_file.write(text + '\n')
        annot = annot.next
text_file.close()

# Close PDF file
pdf_document.close()
