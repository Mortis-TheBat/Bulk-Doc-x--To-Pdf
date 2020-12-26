from docx2pdf import convert 
import os

PATH = "C:/Users/Me/Desktop/WordFiles/"
OUTPUT = "C:/Users/Me/Desktop/ConvertedPdfs/"

print("Attepting to convert files")
def scanning_dir(path):
    count = 0
    docx = 0
    
    print('Scanning the directory')

    dirs = os.listdir(path)
    for item in dirs:
        f, e = os.path.splitext(path+item)
        # print("This is a  = ", e)
        count = count + 1
        if(e==".docx"):
            docx = docx + 1
    # print(count)
    print(f"{count} files found")
    print(f"{docx} Docxx found")

    if(docx > 0):
        convert_to_pdf(path)


def convert_to_pdf(path):
    print("Attempting to convert the found pdfs")
    dirs = os.listdir(path)
    for item in dirs:
        f, e = os.path.splitext(path+item)
        if(e==".docx"):
            print(item)
            convert("C:/Users/Me/Desktop/WordFiles/"+item)
            # convert(item, f+".pdf")
    print("Success")



scanning_dir(PATH)
