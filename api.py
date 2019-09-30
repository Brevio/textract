# -*- coding: utf-8 -*-
import base64
import time
import textract
class Ocr():
    def extract(self, file_in):
        text = textract.process(file_in)
        texto = text.decode('utf-8')
        txt = texto.split('\\n')
        return texto

    def encode(self, image):
        imageFile = open(image, "rb")
        str = base64.b64encode(imageFile.read())
        return str

    def decode(self, imagebase64, fileName1):
        imgdata = base64.b64decode(imagebase64)
        filename = 'media/'+fileName1
        with open(filename, 'wb') as f:
            f.write(imgdata)
        return str(filename)
