from pdf2image import convert_from_path
import pytesseract,pdf2image
import re
import streamlit as st
import pandas as pd
import requests
import json


st.title('INVOICE')
st.markdown("""This app extracts the grand total from the given INVOICE PDFs""")
st.subheader('Convert PDF to Image')
path = st.text_input("Enter Path of the file", "Type Here ...")
 
if(st.button('Submit')):
    # st.success('Path traced!')
    pages = convert_from_path(path, 350, poppler_path=r'C:\Program Files (x86)\poppler-0.68.0\bin')
    for page in pages:
        image_name = "Invoice " + ".jpg"  
        page.save(image_name, "JPEG") 
    # open the pdf file
image = r"D:\DataScience\WEEK 1\Industry Project\Invoice .jpg"
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
st.success(list1)