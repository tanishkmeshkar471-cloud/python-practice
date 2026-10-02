def lower(a):
    st=""
    for i in range(len(a)):
        c = ord(a[i])+32
        d=chr(c)
        st=st+d
    print(st)

def upper(a):
    st=''
    for i in range(len(a)):
        c = ord(a[i])-32
        d=chr(c)
        st=st+d
    print(st)

upper('abc')
lower('ABC')