from docx import Document

if __name__ == '__main__':
    document = Document()
    document.add_paragraph("It was a dark and stormy night.")
    document.add_heading("")
    document.save("dark-and-stormy.docx")



    document = Document("dark-and-stormy.docx")
    content = document.paragraphs[0].text
    print(content)