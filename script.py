from xml.dom import minidom

doc = minidom.parse("xmpl4.xml")

# doc.getElementsByTagName returns NodeList
name = doc.getElementsByTagName("name")[0]
print(name.firstChild.data)

staffs = doc.getElementsByTagName("staff")
for staff in staffs:
        sid = staff.getAttribute("id")
        nickname = staff.getElementsByTagName("nickname")[0]
        salary = staff.getElementsByTagName("salary")[0]
        print("id:%s, nickname:%s, salary:%s" %
              (sid, nickname.firstChild.data, salary.firstChild.data))

# import xml.dom.minidom
  
# docs = xml.dom.minidom.parse("xmpl2.xml") 
  
# # print(docs.nodeName) #document
# print(docs.firstChild.tagName)

# books = docs.getElementsByTagName("book")
# print(books.firstChild.data)
# print([book.getAttribute("country") for book in books])

'''
https://github.com/python/cpython/blob/3.9/Lib/xml/dom/minidom.py

"Warning The xml.dom.minidom module is not secure against maliciously constructed data. 
If you need to parse untrusted or unauthenticated data see XML vulnerabilities."
https://docs.python.org/3/library/xml.dom.minidom.html#module-xml.dom.minidom
'''