from pdf2image import convert_from_path
import pytesseract
import re

for k in range(1,8):
    pdfs = r"D:\DataScience\WEEK 1\Industry Project\pdf\invoice %s.pdf"%(k)
    #print(pdfs)
    pages = convert_from_path(pdfs, 350, poppler_path=r'C:\Program Files (x86)\poppler-0.68.0\bin')
    i = 1
    for page in pages:
        image_name = "Invoice" + str(k) + ".jpg"  
        page.save(image_name, "JPEG")
    i = i+1     
for k in range(1,8):
    # open the pdf file
    image = r"D:\DataScience\WEEK 1\Industry Project\Invoice%s.jpg"%(k)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    x=pytesseract.image_to_string(image)
    file = open('invoice %s.txt'%(k), 'w+')
    file.write(x)
    # print(file.read())
    file.close()
    filename="invoice %s.txt"%(k)
    numbers=[]
    with open(filename, 'r') as f:
        content=f.read()
        numbers.append(re.findall(r"[+-]?[0-9]+\.[0-9]+",content ))
    print(k)
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
    print("  ")