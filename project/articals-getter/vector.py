import string
import re
names=[f'E:\\articals\\prose\\{i}.txt'for i in range(1,2564)]
num=1
stopword=[]
with open("cn_stopwords.txt","r",encoding='utf-8')as f:
    lines=f.readlines()
    for line in lines:
        line=line.strip()
        if len(line)==1:
            stopword.append(line)
with open(r'E:\articals\vector.txt','w',encoding='utf-8')as vctxt:
    for name in names:
        with open(name,'r',encoding='utf-8') as f:
            title=f.readline()
            title=title[1:-2]
            f.readline()
            f.readline()
            lines=f.readlines()
            all_text="".join(lines)
            vector=dict()
            english_puc=string.punctuation
            letters=string.ascii_letters
            all_text=re.sub(r'\W',"",all_text)
            for letter in all_text:
                if letter not in letters:
                    if letter not in stopword:
                        if letter not in vector:
                            vector[letter]=1
                        else:
                            vector[letter]=vector[letter]+1
        sorted(vector.items(),key=lambda item:item[0],reverse=True)
        vctxt.write(str(num)+' '+title+' ')
        num+=1
        vctxt.write(str(vector)[1:-1]+'\n')

