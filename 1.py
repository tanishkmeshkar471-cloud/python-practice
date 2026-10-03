
def upper(a):
    st=''
    for i in range(len(a)):
        if (ord(a[i])>=97 and ord(a[i])<=122):
            c = ord(a[i])-32
            d=chr(c)
            st=st+d
        elif (ord(a[i])>=65 and ord(a[i])<=91):
            c=ord(a[i])+32
            d = chr(c)
            st = st+d
        else:
            st=st+a[i]
    print(st)

def lower(a):
    st=""
    for i in range(len(a)):
        c = ord(a[i])+32
        d=chr(c)
        st=st+d
    print(st)

def upper_lower(a):
    upper(a)
    lower(a)

upper('abcABC12345')
# lower('ABCabc')

#upper_lower('taniSHK')

