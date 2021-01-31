import requests
from bs4 import BeautifulSoup
import re


#các hàm cần thiết

#hàm đọc nôi dung trang web
#kết quả trả về là 1 văn bản dạng chuỗi
def doc_noi_dung(url):
    raw_page = requests.get(url)
    content = BeautifulSoup(raw_page.text, "html.parser")
    return content

#hàm lấy các đường link web trong các nội dung đọc về
#kết quả trả về là một list chứa các link
def lay_duong_link(content):
    a_tag = content.find_all("a")
    result = []
    for item in a_tag:
        link = item.get('href')
        result.append(link)
    return result

#hàm kiểm tra tính hợp lệ của 1 đường link
def kiem_tra_link(link):
    check = re.search("^https", str(link))
    return check
    #for i in link.find_all('href'): #vong for la em kiem tra tung ki tu roi
        #check = i.find('https') #code nay ko dung Thang nhe
        #check =
        #if check is not None:
            #result.append(check)
    #return  #tai sao lai return ma ko co gia tri tra ve?

def chinh_sua_link(url_root, item):
    result  = str(url_root) + str(item)
    return result