from PyPDF2 import PdfFileReader
import glob
import sys
from os.path import exists

def get_info(path):
    try:
        with open(path, 'rb') as f:
            pdf = PdfFileReader(f,strict=False)
            info = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()
        dictionary_items = info.items()
        for item in dictionary_items:
            print("{}: {} ".format(item[0],item[1]))
    except IOError:
        print("Couldnt open a file")
    
def findOutPDF(fileName):
    try:
        binFile = open(fileName,'rb')
        bytes = binFile.read(1024)
        index = ''.join([chr(byte) for byte in bytes]).find('%PDF')
        if index == -1:
            print("Not a PDF header")
            return -1
        return 0
    except IOError:
        print("Couldnt open a file")  

def main(folder):
    if not exists(folder):
        print("Path doesnt exist")
        return 0
    for path in glob.glob(folder+"\\"+"*.pdf"):
        #print(path)
        if not findOutPDF(path):
            #print(path)
            get_info(path)
            print("\n\n")
if __name__ == '__main__':
    main(sys.argv[1])
