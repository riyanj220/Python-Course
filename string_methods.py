a = "riyan!!!!!!!"

print(a.upper())  # ye poori string ko capital kardega
v = "ADFJADBJDBJA"
print(v.isupper())  # saare ke saare characters upper case me hay ke nahi


print(a.lower())  # ye poori string ko lower case me daal dega
g = "asfdafasfsadfa"
print(a.islower())  # saare ke saare characters lowercase me hy ke nahi


ta = "afasfsa asfas fasf asfasfa"
print(ta.title())  # first letter capital kardega yeh poori string ka
fas = "Hello World"
print(
    fas.istitle()
)  # agar poori strinf ka first letter capital hoga to true dega else false


print(
    a.capitalize()
)  # ye pehla letter capital krega sirf aur baki agr koi capital hy to usko small krdega


to = "aafdafa"
print(
    to.swapcase()
)  # upper case ko lower case aur lower case ko upper case me change krdeta ye


print(a.rstrip("!"))  # ye string ke end me chezen cut krdega note:shru me ni krega
print(a.replace("Riyan!!!!!!!", "Riyan"))  # ye replace krdega jis se ap chahty
print(a.split(" "))  # string ko list me convert kardeta hy


python = "welcome to the console"
print(python.center(50))  # for giving spaces or to center something


name = "django  dfafa safasfs django"
print(
    name.count("django")
)  # ik string me particular cheze ki tadaad ko count krne ke liye


str = "welcome $$$"
print(str.endswith("$$$"))


ty = "##afafafa"
print(
    ty.startswith("#")
)  # same as ends with mtlb agr string apki shru jis cheze se  horhi to wo batayega boolean me


tag = "dan adf af asf aa"
print(
    tag.find("adf")
)  # ye index return krta jis pr apka search hoga ,note:string me jb pehli baar ayega tb ka dega ye index dosri tesri baaar ka ni

print(
    tag.index("adf")
)  # similar to find but isme sureity honi chahiye ke lazmi present hy ye hamari string me


z = "Hello123"
print(z.isalnum())  # ye check krta ke apki string alphanumeric hy ke nahi


y = "WrafWfsafW"
print(
    y.isalpha()
)  # ye sirf aplha characters check krta mtlb (small "abcd" or capital "ABCD")


h = "asfdsaf"
print(h.isprintable)  # true karega agr poori string print ho sakti ho
e = "afafsafkash\n"
print(e.isprintable)  # ab isme \n hy to ye false karega ye print nhi hota actual me


str2 = " "
print(str2.isspace())  # isme agr space hogi to ture return karega
