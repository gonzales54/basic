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
        
        import os
        
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(t, path="./hello")

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
