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

        count = count + 1
        if(e==".docx"):
            docx = docx + 1

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
            try:
                convert("C:/Users/Me/Desktop/WordFiles/"+item)
            except:
                print("Unexpected error while converting the .docx file")

        # Uncomment to delete all the docx files that are converted 
            # try:
            #     os.remove(f+e)
            # except:
            #     print("Unexpected error while deleting the .docx file")
            
    print("Success")


scanning_dir(PATH)
