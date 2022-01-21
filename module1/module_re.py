import re


def main():
    s = 'aaa@xxx.com, bbb@yyy.com, ccc@zzz.net'

    m = re.match(r'([a-z]+)@([a-z]+)\.com', s)
    print(m)

    p = re.compile(r'([a-z]+)@([a-z]+)\.com')
    m = p.match(s)
    print(m)

    print("\n")

    s = 'aaa@xxx.com'
    m = re.match(r'[a-z]+@[a-z]+\.[a-z]+', s)
    print(m.start())
    print(m.end())
    print(m.span())
    print(m.group())

    print("\n")

    s = 'aaa@xxx.com, bbb@yyy.com, ccc@zzz.net'
    m = re.match(r'[a-z]+@[a-z]+\.com', s)
    print(m)
    m = re.search(r'[a-z]+@[a-z]+\.com', s)
    print(m)
    m = re.search(r'[a-z]+@[a-z]+\.net', s)
    print(m)
    m = re.search(r'[a-z]+@[a-z]+\.net', s)
    print(m)

    print("\n")

    s = 'aaa@xvx.com'
    m = re.fullmatch(r'[a-z]+@[a-z]+\.com', s)
    print(m)

    print("\n")

    s = 'aaa@xxx.com'
    m = re.findall(r'[a-z]+@[a-z]+\.com$', s)
    print(m)

    print("\n")

    s = 'aaa@xxx.com, bbb@yyy.com, ccc@zzz.net'
    m = re.findall(r'[a-z]+@[a-z]+\.[a-z]+', s)
    print(m)

    print("\n")

    m = re.findall(r'(([a-z]+)@([a-z]+)\.([a-z]+))', s)
    print(m)

    print("\n")

    m = re.finditer(r'[a-z]+@[a-z]+\.[a-z]+', s)
    print(m)
    print(type(m))

    print("\n")

    for f in m:
        print(f)
        print(type(f))

    print("\n")

    l = list(re.finditer(r'[a-z]+@[a-z]+\.[a-z]+', s))
    print(l)

    print([m.span() for m in re.finditer(r'[a-z]+@[a-z]+\.[a-z]+', s)])

    print("\n")

    m = re.sub(r'[a-z]+@[a-z]+\.com', 'new-address', s)
    print(m)

    m = re.sub(r'([a-z]+)@([a-z]+)\.com', r'\1\@\2.net', s)
    print(m)

    m = re.sub(r'(?P<local>[a-z]+)@(?P<SLD>[a-z]+)\.com', r'\g<local>@\g<SLD>.net', s)
    print(m)

    print("\n")

    m = re.sub(r'[a-z]+@[a-z]+\.com', 'new-address', s, count=1)
    print(m)

    m = re.subn(r'[a-z]+@[a-z]+\.com', 'new-address', s)
    print(m)

    print("\n")

    s = '111aaa222bbb333'
    m = re.split('[a-z]+', s)
    print(m)

    m = re.split('[a-z]+', s, 1)
    print(m)

    m = re.split('[0-9]+', s)
    print(m)

    print("\n")

    s = '''aaa-xxx
bbb-yyy
ccc-zzz
        '''

    print(s)

    m = re.findall('[a-z]+', s)
    print(m)

    m = re.findall('^[a-z]+', s)
    print(m)

    m = re.findall('^[a-z]+', s, flags=re.MULTILINE)
    print(m)

    s = 'aaa@xxx.com, bbb@yyy.com'

    m = re.match(r'.+com', s)
    print(m)
    print(m.group())


if __name__ == "__main__":
    main()
