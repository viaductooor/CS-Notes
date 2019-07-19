import os
import re

def process(originalText):

    # remove bottom
    text = re.sub('</br><div align="center">💡 </br></br> 更多精彩内容将发布在公众号.*</img></div>','',originalText,0,re.DOTALL);

    # restore image
    text = re.sub('<div align="center">',' ',text)
    text = re.sub('</div>',' ',text)
    text = re.sub('<br>',' ',text)

    # restore toc
    text = re.sub('<!-- GFM-TOC -->.+<!-- GFM-TOC -->','[TOC]',text,0,re.DOTALL)

    return text


files = os.listdir("../")
for filename in files:
    if '.md' in filename:
        fileUrl = '../'+filename
        text = None
        with open(fileUrl,'r',encoding='utf-8') as file:
            text = file.read()
        text = process(text)
        with open(fileUrl,'w',encoding='utf-8') as file:
            file.write(text)
