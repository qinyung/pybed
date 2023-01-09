from pywebio import *
from pywebio.output import *
from pywebio.input import *

def main():
    #read file
    try: 
        with open ('__foo.ob', 'rb') as fp:
            content1 = fp.read()
    except IOError:
        with open('__foo.ob', 'w') as fp:
            content1 = 'Hello from PyWebIO'
            fp.write(content)
    img = file_upload("上传文件", accept="image/*", placeholder="浏览文件", required=True)
    content = img.get('content')
    type = img.get('mime_type')
#    print(content)
    print(type)
#    with open(img, 'rb') as f:
#        saving = f.read()
    with open('./src/img.png', 'wb') as f:
        f.write(content)
    
    put_file('./src/img.png', content1, 'download link')


if __name__ == '__main__':
    start_server(main, debug=True, port=9999)
#打包exe server = start_server(start, port=8089, auto_open_webbrowser=True, debug=True)
