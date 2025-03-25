from PyPDF2 import PdfReader, PdfWriter

def extract_text(pdf_file):
    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf)

        pdf_text = []

        for page in reader.pages:
        
            words = page.extract_text()
            pdf_text.append(words)

        return pdf_text


def write_txt(lst):

    with open("Descartes.txt", 'w') as f:
        for i in lst:
            f.write(i)


    
if __name__ == '__main__':

    extracted = extract_text("descartes_meditations.pdf")
    write_txt(extracted)
