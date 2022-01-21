import tarfile
import glob
import zipfile

def hello1(): # 圧縮d
    with tarfile.open('hello.tar.gz', 'w:gz') as t:
        t.add('file')

    files = glob.glob('./file/**', recursive=True)
    for file in files:
        print(file)

def hello2():
    with tarfile.open('hello.tar.gz', 'r:gz') as t:
        t.extractall(path='./hello')

def hello3():
    with zipfile.ZipFile('hello.zip', 'w') as new_zip:
        new_zip.write('date/text1.txt', compress_type = zipfile.ZIP_DEFLATED)
        new_zip.write('date/text2.txt', compress_type = zipfile.ZIP_DEFLATED)

def main():
    hello1()
    hello2()
    hello3()

if __name__ == "__main__":
    main()
