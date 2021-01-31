# các hàm cần thiết
import os
import codecs

a = os.chdir('C:\\')
n = len(os.listdir(a))

#các hàm
def folder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)
        print("Folder '{}' đã được tạo.".format(folder))
    os.chdir(folder)

#hàm này tạo tên file tự động, bắt đầu bằng cụm file name tiếp theo là số các file kết thúc là *.html
def tao_ten_file_tu_dong(index):
    k = "Crawl"+ str(index) + ".html"
    return str(k)

#hàm lưu nội dung vào file ở  thư mục chỉ định
def luu_noi_dung(index,data):
    name = "Crawl"+ str(index) + '.html'
    if not os.path.isfile(name):
        file = codecs.open(name , 'w', 'utf8')
        file.write(str(data))
        file.close()