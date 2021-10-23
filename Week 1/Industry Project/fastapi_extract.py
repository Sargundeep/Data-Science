from fastapi import FastAPI,File, UploadFile
from base64 import b64encode
import uvicorn
from pdf2image import convert_from_bytes
from PIL import Image
import pytesseract
import re
app=FastAPI()


@app.post("/")
async def post(file: UploadFile = File(...)):
    pdf_file = await file.read()
    jpg_file = convert(pdf_file)
    return jpg_file


def convert(pdf_file):
    output_folder = "./data"    #create a folder named data
    file_name = "invoice"

    #Convert all pages of PDF to jpg and save
    image_path = convert_from_bytes(
        pdf_file=pdf_file,
        # thread_count=5,
        fmt="jpg",
        output_folder=output_folder,
        output_file=file_name,
        paths_only=True,
        poppler_path=r'C:\Program Files (x86)\poppler-0.68.0\bin'
    )

    #Load all jpg images
    image = [Image.open(image) for image in image_path]
image ="D:\DataScience\WEEK 1\Industry Project\data\invoice0001-1.jpg"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
x=pytesseract.image_to_string(image)
file = open('invoice.txt', 'w+')
file.write(x)
# print(file.read())
file.close()
filename="invoice.txt"
numbers=[]
with open(filename, 'r') as f:
    content=f.read()
    numbers.append(re.findall(r"[+-]?[0-9]+\.[0-9]+",content ))
list1=[]
for number in numbers:
    max=-123456
    for i in number:
        if i !='':
            a=float(i)
            if a > max:
                max=a
    list1.append(max)
print(list1)

@app.get("/get-total")
def get_total():
    return list1

if __name__ == "__main__":
     uvicorn.run(app)