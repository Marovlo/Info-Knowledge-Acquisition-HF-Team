import requests
import lxml
from bs4 import BeautifulSoup

urls=[f'http://www.zuowen.com/gaozhong/gaosan/sanwenshige/index_{i}.shtml' for i in range(2,151)]
headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.41'
}
total_num=0

for url in urls:
    response=requests.get(url=url,headers=headers)
    soup=BeautifulSoup(response.content,'lxml')
    selectors=[f'body > div:nth-child(5) > div > div.artlist_l > div:nth-child({i}) > div.artbox_l_t > a'for i in range(2,22)]
    time_selectors=[f'body > div:nth-child(5) > div > div.artlist_l > div:nth-child({i}) > div.artbox_l_t > span'for i in range(2,22)]
    for selector,time_selector in zip(selectors,time_selectors):
        book_name = soup.select(selector)
        if len(book_name)!=0:
            book_time = soup.select(time_selector)[0].get_text()
            book_name=book_name[0]
            book_url = str(book_name.get("href"))
            book_name=str(book_name.get("title"))
            pos=book_name.find('：')
            if pos==-1:
                pos=0
            else:
                pos=pos+1
            book_name=book_name[pos:book_name.find('_')]
            book_content=requests.get(url=book_url,headers=headers)
            book_soup=BeautifulSoup(book_content.content,'lxml')
            para_selecotrs=[f'body > div:nth-child(7) > div.wrapper_left > div.con_main.wx_dbclick > div.con_content > p:nth-child({i})'for i in range(1,100)]
            text_content=[]
            total_num=total_num+1
            with open(f'E:\\articals\\prose\\{total_num}.txt','w',encoding='utf-8')as f:
                f.write(f"《{book_name}》\n{book_time}\n{book_url}\n")
                for selector in para_selecotrs:
                    para = book_soup.select(selector)
                    if len(para)!=0:
                        para=para[0]
                        para=str(para.get_text())
                        if para[0:7]!='中小学写作指导' and para[0:5]!='作文网专稿' and para[0:5]!='E度网专稿':
                            f.write(para+'\n')
                    else:
                        break
                # time=book_soup.select('body > div:nth-child(7) > div.wrapper_left > div.composition > p')[0]
                # time=time.get_text()[:10]



