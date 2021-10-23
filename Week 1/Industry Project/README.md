# Extraction of Grand Total From Invoice PDFs

[![](https://img.shields.io/badge/Made_with-Python-res?style=for-the-badge&logo=pytorch)](https://docs.python.org/3/)
<!-- [![PWC](https://img.shields.io/endpoint.svg?url=https://fastapi.tiangolo.com/)](https://fastapi.tiangolo.com/)
[![PWC](https://docs.streamlit.io/)](https://docs.streamlit.io/)

<div class='altmetric-embed' data-badge-type='donut' data-arxiv-id='2106.05239'></div>

[![Downloads](https://pepy.tech/badge/invoice)](https://poppler.freedesktop.org/)
 -->
This project is based on extraction of GrandTotal from Invoice PDFs.The basic working of this project includes conversion of PDFs to Images and then to Text. Using RegEX the floating numbers are extracted in a list and the max value is the Grand Total.The entire project is made both with Streamlit and FastAPI.

## Features

- Easy Extraction of Grand Total.
- Minimum Code requirements for extraction of numbers from PDF.
---

---
### Installation for Streamlit :
```
pip install streamlit
pip install pytesseract
pip install pdf2image
pip install pandas

```

### Installation for FastAPI :
```
pip install FastAPI
pip install uvicorn
pip install pillow
pip install streamlit
pip install pytesseract
pip install pdf2image
pip install pandas


```
---

### Making a Virtual Environment:
 ```
 -Step1: Create a Virtual Environment.For this, use the below command
        Command: python3 -m venv <YOUR VIRTUAL ENVIRONMENT NAME>

 -Step2: Activate the Virtual Environment
       Commands: > cd <YOUR VIRTUAL ENVIRONMENT NAME>
                > cd Scripts
                > activate
       These commands will activate the Virtual Environment.
             
                
 ```


<h3 align="center"><b>Developed with :heart: by <a href="https://github.com/Sargundeep">Sargundeep Sachdeo</a>
