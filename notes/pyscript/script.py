import os
import re

files = os.listdir("../")



def process(file,outfile):
    originalText = file.read()

    # remove bottom
    text = re.sub('</br><div align="center">💡 </br></br> 更多精彩内容将发布在公众号.*</img></div>','',originalText,0,re.DOTALL);

    # restore image
    text = re.sub('<div align="center">',' ',text)
    text = re.sub('</div>',' ',text)
    text = re.sub('<br>',' ',text)

    # restore toc
    text = re.sub('<!-- GFM-TOC -->.+<!-- GFM-TOC -->','[TOC]',text,0,re.DOTALL)


    with open(outfile,'w',encoding="utf-8") as of:
        of.write(text)


with open('../缓存.md','r',encoding="utf-8") as f:
    process(f,"../out.md")