from xml.dom import minidom

doc = minidom.parse("xmpl3.xml")

credit = doc.getElementsByTagName("credit")[0]
location = doc.getElementsByTagName("location")[0]
temperature_string = doc.getElementsByTagName("temperature_string")[0]

print(credit.firstChild.data)
print(location.firstChild.data)
print(temperature_string.firstChild.data)

# books = doc.getElementsByTagName("book")
# for book in books:
#         title = book.getElementsByTagName("title")[0]
#         author = book.getElementsByTagName("author")[0]
#         country = book.getAttribute("country")
#         print("Title: %s, Author: %s, Country: %s" % (title.firstChild.data, author.firstChild.data, country) )

'''
https://github.com/python/cpython/blob/3.9/Lib/xml/dom/minidom.py

"Warning The xml.dom.minidom module is not secure against maliciously constructed data. 
If you need to parse untrusted or unauthenticated data see XML vulnerabilities."
https://docs.python.org/3/library/xml.dom.minidom.html#module-xml.dom.minidom
'''