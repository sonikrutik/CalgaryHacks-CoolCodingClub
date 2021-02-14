from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def pdf2Text(filePath):
    pdf = PdfFileReader(filePath)

    with open(f"{filePath[:-3]}txt", "w+", encoding="utf-8") as f:
        for pageNum in range(pdf.numPages):
            print(f"Page: {pageNum}")
            pageObj = pdf.getPage(pageNum)

            try:
                text = pageObj.extractText()
                print("".center(100, "-"))
            except:
                pass
            else:
                print(text)
                f.write(f"Page: {pageNum+1}\n")
                f.write("".center(100, "-"))
                f.write("\n")
                f.write(text)
        
        f.close()

    return


fileDir = os.path.dirname(os.path.realpath('__file__'))
filePath = os.path.join(fileDir, f"parseMaterials/course-outline-Q1.pdf")
pdf2Text(filePath)
