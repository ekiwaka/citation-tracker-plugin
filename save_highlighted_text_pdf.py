from PyPDF2 import PdfReader

# Read pdf file
reader = PdfReader("RTSD.pdf")

for page_num in range(len(reader.pages)):
    page = reader.pages[page_num]

    # If the page has annotations
    if "/Annots" in page:
        print(page_num, "----------------------")
        for annot in page["/Annots"]:
            subtype = annot.get_object()["/Subtype"]

            # If annotation is a highlight
            if subtype == "/Highlight":
                # Get rectangle of annotation
                coords = annot.get_object()["/Rect"]
                # text = ''
                for i in range(0, len(coords)):
                    x1, x2, x3, x4 = coords
                    text = page.extract_text().replace(" ", '').replace("\n", ' ').strip()

                print(text)

